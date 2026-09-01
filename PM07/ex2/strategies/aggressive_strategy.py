from ex0.creatures.creature import Creature
from ex1.creatures.transform_capability import TransformCapability
from .battle_strategy import BattleStrategy
import typing


class AggressiveStrategy(BattleStrategy):

    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        transformer: TransformCapability = typing.cast(
            TransformCapability, creature
        )
        return [
            transformer.transform(),
            creature.attack(),
            transformer.revert()
        ]
