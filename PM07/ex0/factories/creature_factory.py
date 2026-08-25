from ABC import abc, abstractmethod

class Creature(ABC):
    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type = type_

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} ({self.type})"

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Flame")

    def attack(self) -> str:
        return "Flameling attacks with a small flame!"

class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Flame")

    def attack(self) -> str:
        return "Pyrodon unleashes a blazeing inferno!"

class Aquqbub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Tyragon(Creature):

class Sproutling(Creature):

class Bloomelle(Creature):

class Shiftling(Creature):

class Morphagon(Creature):

class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> Creature:
        ...
    @abstractmethod
    def create_evolved()-> Creature:
        ...

class FlameFactory()
class AquaFactory()
class HealingCreatureFactory()
class TransformCreatureFactory()

