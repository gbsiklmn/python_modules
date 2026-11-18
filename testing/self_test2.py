class Counter:
    def __init__(self) -> None:
        self.n = 0

    def show(self) -> None:
        print(id(self))

c1 = Counter()
c2 = Counter()
print(id(c1))
c1.show()
print(id(c2))
c2.show()