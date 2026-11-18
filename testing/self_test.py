def all_positive(values: list[int]) -> bool:
    for v in values:
        if v <= 0:
            return False
    return True

print(all_positive([3, 1, 2]))
print(all_positive([3, -1, 2]))
print(all_positive([]))