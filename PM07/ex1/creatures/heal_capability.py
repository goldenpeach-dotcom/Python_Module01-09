from abc import ABC, abstractmethod
import typing
from ex0.creatures.creature import Creature


class HealCapability(ABC):
    def __init__(self, target: typing.Optional[Creature] = None) -> None:
        self.target = target

    @abstractmethod
    def heal(self, target: typing.Optional[Creature] = None) -> str:
        ...
