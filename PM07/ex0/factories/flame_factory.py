from .creature_factory import CreatureFactory
from ..creatures.creature import Creature
from ..creatures.flame import Flameling, Pyrodon

class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self)-> Creature:
        return Pyrodon()