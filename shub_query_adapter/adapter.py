from api_translator import translate_to_api
from api_requester import send_request
from utils import filter_columns


class ShubQueryAdapter:
    def __init__(self, api_key):
        self.api_key = api_key

    def execute_query(self, query):
        
        select_columns = query["select"]
        from_clause = query["from"]
        where_conditions = query["where"]
        limit_value = query.get("limit")
        
        path_param, params = translate_to_api(from_clause, where_conditions, limit_value)
        raw_data = send_request(path_param, params, self.api_key)
        return filter_columns(raw_data, select_columns)