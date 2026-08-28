#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name: str = name
        self._height: float = round(max(height, 0.0), 1)
        self._age: int = max(age, 0)
        self._stats: "Plant.Stats" = self.Stats()

    @staticmethod
    def is_older_than_year(age_in_days: int) -> bool:
        return age_in_days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount: float = 1.0) -> None:
        if amount > 0:
            self._height = round(self._height + amount, 1)
            self._stats.grow_calls += 1

    def age_up(self, days: int = 1) -> None:
        if days > 0:
            self._age += days
            self._stats.age_calls += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.show_calls += 1

    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0
            self.produce_shade_calls: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )


# ===== Flower =====
class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown",
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


# ===== Seed =====
class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        color: str = "unknown",
    ) -> None:
        super().__init__(name, height, age, color)
        self.number_of_seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.number_of_seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.number_of_seeds}")


# ===== Tree =====
class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        trunk_diameter: float = 0.0,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = round(max(trunk_diameter, 0.0), 1)
        self._stats.produce_shade_calls = 0

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm "
            f"long and {self.trunk_diameter}cm wide."
        )
        self._stats.produce_shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


def display_stats(plant: Plant) -> None:
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._stats.produce_shade_calls} shade")


def main() -> None:
    print("=== Garden statistics ===")

    # Check year-old
    print("=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    # Flower
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)

    # Tree
    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    # Seed
    print("=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_up(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    # Anonymous
    print("=== Anonymous ===")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)


if __name__ == "__main__":
    main()
