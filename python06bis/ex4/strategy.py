from abc import ABC, abstractmethod

from ex3 import Creature, TransformCapability

class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    name: str = "Battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

class NormalStrategy(BattleStrategy):
    name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())