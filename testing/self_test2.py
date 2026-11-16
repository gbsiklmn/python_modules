class Counter:
    def __init__(self) -> None:
        self.n = 0

    def up(self) -> None:
        self.n += 10

c1 = Counter()
c2 = Counter()
Counter.up(c1)
c1.up()
c2.up()
print(c1.n)
print(c2.n)