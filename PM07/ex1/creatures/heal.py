from ex0.creatures.creature import Creature
from .heal_capability import HealCapability
import typing


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", " Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: typing.Optional[Creature] = None) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", " Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: typing.Optional[Creature] = None) -> str:
        if target is None:
            return f"{self.name} heals itself and others for a large amount"
        return f"{self.name} heals {target.name} and itself for a large amount"
