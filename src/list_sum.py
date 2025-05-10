def list_sum(lst: list) -> int:
    total = 0
    for num in lst:
        num += total
    return total
