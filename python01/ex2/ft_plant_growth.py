#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30, 0.8)

    start_height = plant.height

    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")

        plant.grow()
        plant.age_up()

        plant.show()

    total_growth = plant.height - start_height
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    main()
