from query_parser import parse_query
from api_translator import translate_to_api
from api_requester import send_request
from utils import filter_columns

class ShubSQLAdapter:
    def __init__(self, api_key):
        self.api_key = api_key

    def execute_query(self, sql_query):
        select_columns, from_clause, where, limit = parse_query(sql_query)
        path_param, params = translate_to_api(from_clause, where, limit)
        raw_data = send_request(path_param, params, self.api_key)
        return filter_columns(raw_data, select_columns)