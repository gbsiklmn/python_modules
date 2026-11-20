from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def print_lineup(opponents: list[tuple[CreatureFactory,
                                       BattleStrategy]]) -> None:
    labels: list[str] = []
    for factory, strategy in opponents:
        labels.append(f"({factory.create_base().name}+{strategy.name})")
    print(" [ "+", ".join(labels) + " ]")


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                a = factory_a.create_base()
                b = factory_b.create_base()
                print("\n* Battle *")
                print(a.describe())
                print(" vs.")
                print(b.describe())
                print(" now fight!")
                strategy_a.act(a)
                strategy_b.act(b)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    basic: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame, normal),
        (transform, aggressive),
    ]
    print_lineup(basic)
    battle(basic)

    print("\nTournament 1 (error)")
    error: list[tuple[CreatureFactory, BattleStrategy]] = [
        (transform, aggressive),
        (flame, aggressive),
    ]
    print_lineup(error)
    battle(error)


if __name__ == "__main__":
    main()
