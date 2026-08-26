from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type = type_

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"



# class Sproutling(Creature):

# class Bloomelle(Creature):

# class Shiftling(Creature):

# class Morphagon(Creature):


# class FlameFactory()
# class AquaFactory()
# class HealingCreatureFactory()
# class TransformCreatureFactory()

