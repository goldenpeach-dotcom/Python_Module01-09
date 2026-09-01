from ex0.factories.creature_factory import CreatureFactory
from ..creatures.heal import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()
