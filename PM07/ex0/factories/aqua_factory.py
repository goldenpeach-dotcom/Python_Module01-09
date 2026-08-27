from .creature_factory import CreatureFactory
from ..creatures.creature import Creature
from ..creatures.aqua import Aquabub, Torragon


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self)-> Creature:
        return Torragon()