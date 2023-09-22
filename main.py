import sys
import json
from query_parser import parse_query
from api_translator import translate_to_api
from api_requester import send_request
from utils import filter_columns

def execute_query(sql_query):
    select_columns, from_clause, where, limit = parse_query(sql_query)
    path_param, params = translate_to_api(from_clause, where, limit)
    raw_data = send_request(path_param, params)
    return filter_columns(raw_data, select_columns)

def write_to_file(filename, data, mode):
    with open(filename, mode) as f:
        if isinstance(data, list) or isinstance(data, dict):
            json.dump(data, f)
        else:
            f.write(str(data))

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "-q":
        query = sys.argv[2]
        
        output_file = None
        write_mode = None
        
        if "-o" in sys.argv:
            output_file = sys.argv[sys.argv.index("-o") + 1]
            write_mode = "a"
        elif "-O" in sys.argv:
            output_file = sys.argv[sys.argv.index("-O") + 1]
            write_mode = "w"
        
        try:
            result = execute_query(query)
            print(result)
            
            if output_file and write_mode:
                write_to_file(output_file, result, write_mode)
            
            exit(0)
        except Exception as e:
            print(f"Error: {e}")
            
    print("Please enter your SQL query (or type 'exit' to quit):")
    
    while True:
        query = input(">>> ")
        
        if query.lower() == 'exit':
            break
        
        if query == '':
            continue
        
        try:
            print(execute_query(query))
        except Exception as e:
            print(f"Error: {e}")