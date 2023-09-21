import sqlparse

def parse_query(sql_query):
    parsed = sqlparse.parse(sql_query)[0]

    from_clause = None
    where_conditions = []
    limit = None

    tokens = [token for token in parsed.tokens if not token.is_whitespace]

    for i, token in enumerate(tokens):

        if token.value.upper() == "SELECT":
            columns = tokens[i+1].value.strip()
            select_columns = [col.strip() for col in columns.split(",")]

        if token.value.upper() == "FROM":
            from_clause = tokens[i+1].value.strip()
        
        if "WHERE" in token.value.upper():
            where_clause = token.value.split("WHERE")[1].strip()
            conditions = where_clause.split("AND")
            for condition in conditions:
                where_conditions.append(condition.strip())
                            
        if "LIMIT" in token.value.upper():
            limit = int(tokens[i+1].value.strip())

    return select_columns, from_clause, where_conditions, limit
