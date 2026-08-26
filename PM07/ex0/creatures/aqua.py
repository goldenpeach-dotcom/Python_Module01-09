from ex0.creatures.creature import Creature

class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
