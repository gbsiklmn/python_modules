def ft_count_harvest_iterative():
    target = int(input("Days until harvest: "))
    for day in range(1, target + 1):
        print(f"Day {day}")
    print("Harvest time!")
