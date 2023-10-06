from .api_translator import translate_to_api
from .api_requester import get_items_request, get_job_stats_request
from .utils import filter_columns, generate_unique_random_numbers

import concurrent.futures

class ShubQueryAdapter:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def _parse_query(self, query):
        select_columns = query["select"]
        from_clause = query["from"]
        where_conditions = query.get("where")
        total_count = query.get("total_count")
        limit_value = query.get("limit", 1)
        start_after = query.get("start_after")
        return select_columns, from_clause, where_conditions, limit_value, start_after, total_count
    

    def execute_query(self, query):
        select_columns, from_clause, where_conditions, limit_value, start_after, total_count = self._parse_query(query)
        path_param, params = translate_to_api(from_clause, where_conditions, limit_value, start_after)

        raw_data = get_items_request(path_param, params, self.api_key)
        return filter_columns(raw_data, select_columns)


    def _fetch_data(self, start_value, path_param, params):
        params['startafter'] = f"{path_param}/{start_value}"
        return get_items_request(path_param, params, self.api_key)

    def execute_query_random(self, query):
        select_columns, from_clause, where_conditions, limit_value, start_after, total_count = self._parse_query(query)
        path_param, params = translate_to_api(from_clause, where_conditions, 1, start_after)

        if (total_count == None):
            try:
                total_items_count = get_job_stats_request(path_param, self.api_key)['scrapystats']['consumers_processed_items']
            except KeyError:
                raise ValueError(f"Failed to get total item count from API response.")
        else:
            total_items_count = total_count
        
        random_start_after = generate_unique_random_numbers(total_items_count, limit_value)
        
        aggregated_raw_data = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._fetch_data, start_value, path_param, params.copy()) for start_value in random_start_after]
            for future in concurrent.futures.as_completed(futures):
                data = future.result()
                if isinstance(data, list):
                    aggregated_raw_data.extend(data)

        return filter_columns(aggregated_raw_data, select_columns)
