import sqlparse

def parse_query(sql_query):
    parsed = sqlparse.parse(sql_query)[0]

    from_clause = None
    where = None
    limit = None

    tokens = [token for token in parsed.tokens if not token.is_whitespace]

    for i, token in enumerate(tokens):
        if token.value.upper() == "FROM":
            from_clause = tokens[i+1].value.strip()
        
        if "WHERE" in token.value.upper():
            where = token.value.split("WHERE")[1].strip()
            
        if "LIMIT" in token.value.upper():
            limit = int(tokens[i+1].value.strip())

    return from_clause, where, limit
