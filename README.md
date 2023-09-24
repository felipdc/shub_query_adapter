# Shub Query Adapter

The `shub_query_adapter` is a Python project that provides an interface to query data from the Scrapinghub storage API. It allows users to build and execute queries in a more readable and structured manner, abstracting away the complexities of the underlying API.

## Installation

To use the `shub_query_adapter`, you can install via pip:

```bash
pip install shub_query_adapter
```

## Usage

### 1. Building a Query

Use the `QueryBuilder` class to construct your query:

```python
from query_builder import QueryBuilder

query = (QueryBuilder()
         .select(["name", "price"])
         .from_("684510/2/17")
         .where("name").contains("laptop")
         .and_("price").lt("1000")
         .limit(10)
         .build())
```

### 2. Executing the Query

Once you have your query, you can use the `ShubQueryAdapter` to execute it:

```python
from adapter import ShubQueryAdapter

adapter = ShubQueryAdapter(api_key="YOUR_API_KEY")
results = adapter.execute_query(query)
print(results)
```

## Supported Operators

The `QueryBuilder` supports a variety of operators:

- `equals(value)`: Checks if the field is equal to the given value.
- `gt(value)`: Checks if the field is greater than the given value.
- `gte(value)`: Checks if the field is greater than or equal to the given value.
- `lt(value)`: Checks if the field is less than the given value.
- `lte(value)`: Checks if the field is less than or equal to the given value.
- `exists()`: Checks if the field exists.
- `not_exists()`: Checks if the field does not exist.
- `not_equal(value)`: Checks if the field is not equal to the given value.
- `contains(value)`: Checks if the field contains the given value.
- `icontains(value)`: Case-insensitive check if the field contains the given value.
