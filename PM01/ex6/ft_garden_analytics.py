#!/usr/bin/env python3

DEFAULT_HEIGHT = 0.0
DEFAULT_AGE = 0

class Plant:

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float
    ) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._height = DEFAULT_HEIGHT
        self.set_height(height, is_init=True)
        self._days = DEFAULT_AGE
        self.set_age(days, is_init=True)

        self.__stats = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self._grow_cnt: int = 0
            self._age_cnt: int = 0
            self._show_cnt: int = 0

    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous_make(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, days=0, growth_rate=0.0)

    def get_stats(self) -> "Plant.Stats":
        return self.__stats

    def grow(self, days: int = 1) -> None:
        self.__stats._grow_cnt += 1
        self._height += self._growth_rate * days

    def age(self, days: int = 1) -> None:
        self.__stats._age_cnt += 1
        self._days += days

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
        self._height = float(h)
        if not is_init:
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, d: int,is_init: bool = False) -> None:
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
        self._days = d
        if not is_init:
            print(f"Age updated: {d} days")

    def show(self) -> None:
        self.__stats._show_cnt += 1
        print(
            f"{self._name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def grow_and_age_for(self, days: int) -> None:
        self.grow(days)
        self.age(days)


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
        print(f" Color: {self._color}")
        if self._bloomed == 0:
            print(f" {self._name.capitalize()} has not bloomed yet")
        if self._bloomed == 1:
            print(f" {self._name.capitalize()} is blooming beautifully!")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float,
        color: str,
        seed_count: int = 0
    ) -> None:
        super().__init__(name, height, days, growth_rate, color)
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        if self._bloomed == 1:
            self._seed_count = 42
        else:
            self._seed_count = 0
        print(f" Seeds: {self._seed_count}")

    def grow_and_age_for(self, days: int) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        super().grow_and_age_for(days)
        self.bloom()


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

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_cnt = 0

    def get_stats(self) -> "Tree.Stats":
        stats = super().get_stats()
        assert isinstance(stats, Tree.Stats)
        return stats

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        if self.get_height() > 0 and self._trunk_diameter > 0:
            print(
                f"Tree {self._name.capitalize()} now produces a shade of "
                f"{round(self.get_height(), 1):.1f}cm long and "
                f"{round(self._trunk_diameter, 1):.1f}cm wide."
            )
            self.get_stats()._shade_cnt = 1
        else:
            print(f"{self._name.capitalize()} can't produce shade!")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1):.1f}cm")


def display_stats(plant) -> None:
    stats = plant.get_stats()
    print(f"[statistics for {plant._name.capitalize()}]")
    print(
        f"Stats: {stats._grow_cnt} grow, "
        f"{stats._age_cnt} age, "
        f"{stats._show_cnt} show"
    )
    if isinstance(plant, Tree):
        tree_stats = plant.get_stats()
        print(f" {tree_stats._shade_cnt} shade")


def main() -> None:
    f = Flower("rose", 15, 10, 8.0, "red")
    t = Tree("oak", 200, 365, 0.8, 5)
    s = Seed("sunflower", 80.0, 45, 1.5, "yellow")
    # v = Vegetable("tomato", 5.0, 10, 2.1, "April")

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year?-> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year?-> {Plant.check_year_old(400)}")
    print()
    print("=== Flower")
    f.show()
    display_stats(f)
    print(f"[asking the {f._name} to grow and bloom]")
    f.grow()
    f.bloom()
    f.show()
    display_stats(f)
    print()
    print("=== Tree")
    t.show()
    display_stats(t)
    t.produce_shade()
    display_stats(t)
    print()
    print("=== Seed")
    s.show()
    s.grow_and_age_for(20)
    s.show()
    display_stats(s)
    print()
    print("=== Anonymous")
    u = Plant.anonymous_make()
    u.show()
    display_stats(u)

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
