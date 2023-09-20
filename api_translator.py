import json

def translate_operator(op, field, value):
    
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]  # Strip the quotes
    # If not, try to convert the value to an integer
    else:
        try:
            value = int(value)
        except ValueError:
            pass
        
    if op in ['=', '<', '>', '<=', '>=', '!=']:
        return [field, op, [value]]
    elif op == 'exists':
        return [field, "exists"]
    elif op == 'notexists':
        return [field, "notexists"]
    elif op == 'contains':
        return [field, "contains", [value]]
    elif op == 'icontains':
        return [field, "icontains", [value]]
    elif op == 'isempty':
        return [field, "isempty"]
    elif op == 'isnotempty':
        return [field, "isnotempty"]
    elif op == 'matches':
        return [field, "matches", [value]]
    elif op == 'haselement':
        return [field, "haselement", [value]]
    elif op == 'hasnotelement':
        return [field, "hasnotelement", [value]]
    else:
        raise ValueError(f"Unsupported operator: {op}")

def translate_to_api(from_clause, where, limit):
    filters = []
    
    if where:
        # A more advanced parser would be needed for complex where clauses.
        field, op, value = where.split()
        filter_value = translate_operator(op, field, value)
        filters.append(json.dumps(filter_value))

    params = {
        'filter': filters
    }

    if limit:
        params['count'] = limit

    path_param = from_clause

    # print(params)
    return path_param, params
