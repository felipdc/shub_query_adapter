class QueryBuilder:
    def __init__(self):
        self.select_columns = []
        self.from_table = None
        self.where_conditions = []
        self.limit_value = None
        self.start_after = None
        self.total_count_value = None
        self._current_field = None

    def select(self, columns = []):
        self.select_columns = columns
        return self
    
    def random(self):
        self.start_after = 'random'
        return self

    def from_(self, table):
        self.from_table = table
        return self

    def where(self, field):
        self._current_field = field
        return self

    def and_(self, field):
        return self.where(field)

    def equals(self, value):
        self._append_condition("=", value)
        return self
    
    def gt(self, value):
        self._append_condition(">", value)
        return self

    def gte(self, value):
        self._append_condition(">=", value)
        return self

    def lt(self, value):
        self._append_condition("<", value)
        return self

    def lte(self, value):
        self._append_condition("<=", value)
        return self

    def exists(self):
        self._append_condition("exists", None)
        return self

    def not_exists(self):
        self._append_condition("notexists", None)
        return self

    def not_equal(self, value):
        self._append_condition("!=", value)
        return self

    def contains(self, value):
        self._append_condition("contains", value)
        return self

    def icontains(self, value):
        self._append_condition("icontains", value)
        return self

    def limit(self, value):
        self.limit_value = value
        return self
    
    def total_count(self, value):
        self.total_count_value = value
        return self

    def _append_condition(self, operator, value):
        if self._current_field is None:
            raise ValueError("No field specified for condition")
        condition = f"{self._current_field} {operator}"
        if value is not None:
            condition += f' "{value}"'
        self.where_conditions.append(condition)
        self._current_field = None

    def build(self):
        query = {
            "select": self.select_columns,
            "from": self.from_table,
            "where": self.where_conditions
        }
        if self.limit_value:
            query["limit"] = self.limit_value
        if self.start_after:
            query["start_after"] = self.start_after
        if self.total_count_value:
            query["total_count"] = self.total_count_value
        return query
