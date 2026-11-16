class Dog:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print(f"{self.name} says woof")

a = Dog("Rex")
b = Dog("Luna")
a.speak()
b.speak()