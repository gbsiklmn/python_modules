def harvest_helper(current_day, target_day):
    if current_day > target_day:
        return
    print(f"Day {current_day}")
    harvest_helper(current_day + 1, target_day)


def ft_count_harvest_recursive():
    target = int(input("Days until harvest: "))
    harvest_helper(1, target)
    print("Harvest time!")
