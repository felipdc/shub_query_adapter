import json
import re

def translate_operator(op, field, value):
    
    if value:
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        else:
            try:
                value = int(value)
            except ValueError:
                pass
    
    if op in ['=', '<', '>', '<=', '>=', '!=']:
        return [field, op, [value]]
    elif op == 'exists':
        return [field, "exists", []]
    elif op == 'notexists':
        return [field, "notexists", []]
    elif op == 'contains':
        return [field, "contains", [value]]
    elif op == 'icontains':
        return [field, "icontains", [value]]
    elif op == 'isempty':
        return [field, "isempty", []]
    elif op == 'isnotempty':
        return [field, "isnotempty", []]
    elif op == 'matches':
        return [field, "matches", [value]]
    elif op == 'haselement':
        return [field, "haselement", [value]]
    elif op == 'hasnotelement':
        return [field, "hasnotelement", [value]]
    else:
        raise ValueError(f"Unsupported operator: {op}")

def translate_to_api(from_clause, where, limit, start_after):
    filters = []
    
    for condition in where:
        match = re.match(r'(\w+)\s*([=<>!|contains|icontains]+|exists|notexists|isempty|isnotempty)\s*(?:"(.*?)"|(\d+)|$)', condition)
        if match:
            field, op, value_str, value_num = match.groups()
            value = value_str if value_str is not None else value_num
        else:
            raise ValueError(f"Invalid condition: {condition}")
        
        filter_value = translate_operator(op, field, value)
        filters.append(json.dumps(filter_value))

    params = {
        'filter': filters
    }

    if limit:
        params['count'] = limit
        
    if start_after:
        params['startafter'] = start_after

    path_param = from_clause

    return path_param, params
