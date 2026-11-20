from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    print("Testing battle")
    a = first.create_base()
    b = second.create_base()
    print(a.describe())
    print(" vs.")
    print(b.describe())
    print(" fight!")
    print(a.attack())
    print(b.attack())


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    test_factory(flame)
    print()
    test_factory(transform)
    print()
    test_battle(flame, transform)


if __name__ == "__main__":
    main()
