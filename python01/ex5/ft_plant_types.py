#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0

    def grow(self, amount: float = 1.0) -> None:
        if amount > 0:
            self._height += amount

    def age_up(self, days: int = 1) -> None:
        if days > 0:
            self._age += days

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


# ===== Flower =====
class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown"
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.has_bloomed: bool = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


# ===== Tree =====
class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        trunk_diameter: float = 0.0
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter if trunk_diameter >= 0 else 0.0

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


# ===== Vegetable =====
class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        harvest_season: str = "unknown"
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, amount: float = 1.0) -> None:
        if amount > 0:
            super().grow(amount)

    def age_up(self, days: int = 1) -> None:
        if days > 0:
            super().age_up(days)
            self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    # Flower
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    # Tree
    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    # Vegetable
    print("=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age_up(1)
    tomato.show()


if __name__ == "__main__":
    main()
