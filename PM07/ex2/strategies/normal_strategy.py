from ex0.creatures.creature import Creature
# from ex1.creatures.heal import HealCapability
# from ex1.creatures.transform import TransformCapability
from .battle_strategy import BattleStrategy


class NormalStrategy(BattleStrategy):

    name = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        self._reject_invalid(creature)
        return [creature.attack()]
