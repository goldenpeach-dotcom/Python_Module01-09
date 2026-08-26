from abc import ABC, abstractmethod
from ex0.creatures.creature import Creature

class CreatureFactory(ABC):
    
    @abstractmethod
    def create_base() -> Creature:
        ...
    @abstractmethod
    def create_evolved()-> Creature:
        ...

# class FlameFactory()
# class AquaFactory()
# class HealingCreatureFactory()
# class TransformCreatureFactory()

