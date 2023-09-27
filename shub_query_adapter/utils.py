import random

def filter_columns(data, select_columns = []):
    if len(select_columns) == 0:
        return data
    
    filtered_data = []
    for item in data:
        filtered_item = {col: item[col] for col in select_columns if col in item}
        filtered_data.append(filtered_item)

    return filtered_data

def generate_unique_random_numbers(total_items_count, limit_value):
    if limit_value > total_items_count:
        raise ValueError("Cannot generate more unique numbers than the total item count")

    return random.sample(range(1, total_items_count + 1), limit_value)