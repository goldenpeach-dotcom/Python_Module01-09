from .creature_factory import CreatureFactory
from ex0.creatures.creature import Creature
from ex0.creatures.flame import Flameling, Pyrodon

class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self)-> Creature:
        return Pyrodon()