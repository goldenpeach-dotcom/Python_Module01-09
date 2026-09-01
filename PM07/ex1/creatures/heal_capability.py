from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self, target: str) -> None:
        self.target = target

    @abstractmethod
    def heal(self) -> str:
        ...
