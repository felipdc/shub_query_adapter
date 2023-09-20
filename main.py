from query_parser import parse_query
from api_translator import translate_to_api
from api_requester import send_request

def execute_query(sql_query):
    from_clause, where, limit = parse_query(sql_query)
    path_param, params = translate_to_api(from_clause, where, limit)
    print(path_param, params)
    return send_request(path_param, params)

if __name__ == "__main__":
    query = "SELECT * FROM 684510/1/20 WHERE heading exists limit 5"
    print(execute_query(query))
