def filter_columns(data, select_columns):
    if "*" in select_columns:
        return data

    filtered_data = []
    for item in data:
        filtered_item = {col: item[col] for col in select_columns if col in item}
        filtered_data.append(filtered_item)

    return filtered_data
