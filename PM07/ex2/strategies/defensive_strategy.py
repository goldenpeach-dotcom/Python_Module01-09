from ex0.creatures.creature import Creature
from ex1.creatures.heal_capability import HealCapability
# from .invalid_strategy_error import InvalidStrategyError
from .battle_strategy import BattleStrategy
import typing


class DefensiveStrategy(BattleStrategy):

    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        healer: HealCapability = typing.cast(HealCapability, creature)
        return [creature.attack(), healer.heal()]
