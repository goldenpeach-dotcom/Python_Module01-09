#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._height = 0.0
        self._days = 0

        if height < 0:
            print(f"{name.capitalize()}: Error, height can't be negative")
        elif height > 1000:
            print(f"{name.capitalize()}: Error, height can't be too big")
        else:
            self._height = float(height)

        if days < 0:
            print(f"{name.capitalize()}: Error, age can't be negative")
        elif days > 1000:
            print(f"{name.capitalize()}: Error, age can't be too long")
        else:
            self._days = days

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
            return
        elif h > 1000:
            print(f"{self.name.capitalize()}: Error, height can't be too big")
            print("Height update rejected")
            return
        else:
            self._height = float(h)
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, d: int) -> None:
        if d < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        elif d > 1000:
            print(f"{self.name.capitalize()}: Error, age can't be too long")
            print("Age update rejected")
            return
        else:
            self._days = d
            print(f"Age updated: {d} days")

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float,
        color: str
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self._bloomed = 0

    def bloom(self) -> None:
        self._bloomed = 1
        print(f"[asking the {self.name} to bloom]")
        self.show()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed == 0:
            print(f"{self.name.capitalize()} has not bloomed yet")
        if self._bloomed == 1:
            print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        if self.get_height() > 0 and self.trunk_diameter > 0:
            print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{round(self.get_height(), 1):.1f}cm long and "
                f"{round(self.trunk_diameter, 1):.1f}cm wide."
            )
        else:
            print(f"{self.name.capitalize()} can't produce shade!")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1):.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow_and_age_for(self, days: int) -> int:
        print(f"[make {self.name} grow and age for {days} days]")
        for _ in range(days):
            self.grow()
            self.age()
        return self.nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {int(self.nutritional_value)}")


if __name__ == "__main__":
    f = Flower("rose", 15, 10, 0.1, "red")
    t = Tree("oak", 200, 365, 0.8, 5)
    s = Tree("spine", 430, 925, 0.5, 5)
    v = Vegetable("tomato", 5.0, 10, 2.1, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    f.show()
    f.bloom()
    print("=== Tree")
    t.show()
    t.produce_shade()
    print("=== Vegetable")
    v.show()
    v.grow_and_age_for(20)
    v.show()

# === Garden Plant Types ===
# === Flower
# Rose: 15.0cm, 10 days old
# Color: red
# Rose has not bloomed yet
# [asking the rose to bloom]
# Rose: 15.0cm, 10 days old
# Color: red
# Rose is blooming beautifully!
# === Tree
# Oak: 200.0cm, 365 days old
# Trunk diameter: 5.0cm
# [asking the oak to produce shade]
# Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
# === Vegetable
# Tomato: 5.0cm, 10 days old
# Harvest season: April
# Nutritional value: 0
# [make tomato grow and age for 20 days]
# Tomato: 47.0cm, 30 days old
# Harvest season: April
# Nutritional value: 20
