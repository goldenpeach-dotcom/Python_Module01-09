from abc import ABC, abstractmethod
from ex0.creatures.creature import Creature
from .invalid_strategy_error import InvalidStrategyError


class BattleStrategy(ABC):

    name: str = "battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...

    def _reject_invalid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this {self.name} strategy"
            )
