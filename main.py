from query_parser import parse_query
from api_translator import translate_to_api
from api_requester import send_request
from utils import filter_columns

def execute_query(sql_query):
    select_columns, from_clause, where, limit = parse_query(sql_query)
    path_param, params = translate_to_api(from_clause, where, limit)
    raw_data = send_request(path_param, params)
    return filter_columns(raw_data, select_columns)

if __name__ == "__main__":
    query = 'SELECT * FROM 435191/864/42 WHERE domain = "at" limit 1'
    print(execute_query(query))
