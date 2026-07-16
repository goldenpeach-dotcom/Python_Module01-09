#!/usr/bin/env python3

class Plant:

    class Stats:
        def __init__ (self):
            self.grow_cnt: int = 0
            self.age_cnt: int = 0
            self.show_cnt: int = 0

        def display(self):
            print(
                f"Stats: {self.grow_cnt} grow, "
                f"{self.age_cnt} age, "
                f"{self.show_cnt} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float
    ) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._height = 0.0
        self._days = 0
        self.__stats = Plant.Stats()

        self.set_height(height, is_init=True)
        self.set_age(days, is_init=True)

    @staticmethod
	def check_year_old(self) -> int:
		return _days > 365
	
	@classmethod
	def anonymous_make(cls) -> Self:
        return cls("Unknown plant", 0.0, 0)

    def get_stats(self):
        return self.__stats

    def grow(self) -> None:
        self.__stats._grow_cnt += 1
        self._height += self._growth_rate

    def age(self) -> None:
        self.__stats._age_cnt += 1
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, h: float, is_init: bool = False) -> None:
        if h < 0:
            print(
                f"{self._name.capitalize()}: "
                f"Error, height can't be negative")
            if not is_init:
                print("Height update rejected")
            return
        elif h > 1000:
            print(f"{self._name.capitalize()}: Error, height can't be too big")
            if not is_init:
                print("Height update rejected")
            return
        else:
            self._height = float(h)
            if not is_init:
                print(f"Height updated: {int(self._height)}cm")

    def set_age(self, d: int, is_init: bool = False) -> None:
        if d < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            if not is_init:
                print("Age update rejected")
            return
        elif d > 1000:
            print(f"{self._name.capitalize()}: Error, age can't be too long")
            if not is_init:
                print("Age update rejected")
            return
        else:
            self._days = d
            if not is_init:
                print(f"Age updated: {d} days")

    def show(self) -> None:
        self.__stats.show_cnt += 1
        print(
            f"{self._name.capitalize()}: {round(self.get_height(), 1)}cm, "
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
        self._color = color
        self._bloomed = 0

    def bloom(self) -> None:
        self._bloomed = 1

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed == 0:
            print(f"{self._name.capitalize()} has not bloomed yet")
        if self._bloomed == 1:
            print(f"{self._name.capitalize()} is blooming beautifully!")


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
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        if self.get_height() > 0 and self._trunk_diameter > 0:
            print(
                f"Tree {self._name.capitalize()} now produces a shade of "
                f"{round(self.get_height(), 1):.1f}cm long and "
                f"{round(self._trunk_diameter, 1):.1f}cm wide."
            )
        else:
            print(f"{self._name.capitalize()} can't produce shade!")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1):.1f}cm")


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
        self._harvest_season = harvest_season
        self._nutritional_value: float = 0

    def grow_and_age_for(self, days: int) -> float:
        print(f"[make {self._name} grow and age for {days} days]")
        for _ in range(days):
            self.grow()
            self.age()
        return self._nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {int(self._nutritional_value)}")

def display_stats(Plant)
	print(
		f"Stats: {grow()が呼ばれた数} grow,"
		f" {age()が呼ばれた数} age, "
		f"{bloom()produce_shade()seed()呼ばれた数}"
	)

def main() -> None:
    f = Flower("rose", 15, 10, 0.1, "red")
    t = Tree("oak", 200, 365, 0.8, 5)
    v = Vegetable("tomato", 5.0, 10, 2.1, "April")

    print("=== Garden statistics ===")
	print("=== Check year-old")
	print("Is 30 days more than a year? -> False")
	print("Is 400 days more than a year? -> True")

    print("=== Flower")
    f.show()
    print(f"[asking the {f._name} to bloom]")
    f.bloom()
    f.show()
    print()
    print("=== Tree")
    t.show()
    t.produce_shade()
    print()
    print("=== Vegetable")
    v.show()
    v.grow_and_age_for(20)
    v.show()


if __name__ == "__main__":
    main()


# $> python3 ft_garden_analytics.py
# === Garden statistics ===
# === Check year-old
# Is 30 days more than a year? -> False
# Is 400 days more than a year? -> True
# === Flower
# Rose: 15.0cm, 10 days old
# Color: red
# Rose has not bloomed yet
# [statistics for Rose]
# Stats: 0 grow, 0 age, 1 show
# [asking the rose to grow and bloom]
# Rose: 23.0cm, 10 days old
# Color: red
# Rose is blooming beautifully!
# [statistics for Rose]
# Stats: 1 grow, 0 age, 2 show
# === Tree
# Oak: 200.0cm, 365 days old
# Trunk diameter: 5.0cm
# [statistics for Oak]
# Stats: 0 grow, 0 age, 1 show
# 0 shade
# [asking the oak to produce shade]
# Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
# [statistics for Oak]
# Stats: 0 grow, 0 age, 1 show
# 1 shade
# === Seed
# Sunflower: 80.0cm, 45 days old
# Color: yellow
# Sunflower has not bloomed yet
# Seeds: 0
# [make sunflower grow, age and bloom]
# Sunflower: 110.0cm, 65 days old
# Color: yellow
# Sunflower is blooming beautifully!
# Seeds: 42
# [statistics for Sunflower]
# Stats: 1 grow, 1 age, 2 show
# === Anonymous
# Unknown plant: 0.0cm, 0 days old
# [statistics for Unknown plant]