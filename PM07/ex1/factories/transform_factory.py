from ex0.factories.creature_factory import CreatureFactory
from ex0.creatures.creature import Creature
from ..creatures.transform import Shiftling, Morphagon

class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self)-> Morphagon:
        return Morphagon()