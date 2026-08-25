from .creature import Creature

class Aquqbub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Tyragon(Creature):
     def __init__(self):
        super().__init__("Tyragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"