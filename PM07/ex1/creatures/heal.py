from ex0.creatures.creature import Creature
from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self, target: str) -> None:
        self.target = target
        
    @abstractmethod
    def heal(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", " Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature):
    def __init__(self) -> None:
        super().__init__("Bloomelle", " Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"