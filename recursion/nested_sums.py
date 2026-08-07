def sum_nested_list(lst: list[int | list]) -> int:
    total_size: int = 0
    for item in lst:
        if isinstance(item, list):
            total_size += sum_nested_list(item)
        else:
            total_size += item
    return total_size
