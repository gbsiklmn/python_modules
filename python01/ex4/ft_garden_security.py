#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.get_height()}cm, {plant.get_age()} days old")
    plant.set_height(25.0)
    plant.set_age(30)
    plant.set_height(-5.0)
    plant.set_age(-10)
    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    main()
