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

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def get_name(self) -> str:
        return self._name

    def set_height(self, h: float, is_init: bool = False) -> None:
        if h < 0:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, height can't be negative")
            if not is_init
                print("Height update rejected")
            return
        elif h > 1000:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, height can't be too big"
            )
            if not is_init
                print("Height update rejected")
            return
        self._height = float(h)
        if not is_init:
            print(f"Height updated: {int(self.get_height())}cm")

    def set_age(self, d: int,  is_init: bool = False) -> None:
        if d < 0:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, age can't be negative"
            )
            if not is_init
                print("Age update rejected")
            return
        elif d > 1000:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, age can't be too long"
            )
            if not is_init
                print("Age update rejected")
            return
        self._days = d
        if not is_init:
            print(f"Age updated: {d} days")

    def show(self) -> None:
        print(
            f"{self.get_name().capitalize()}: "
            f"{round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        color: str,
        growth_rate: float
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self._color = color
        self._bloomed = 0

    def bloom(self) -> None:
        self._bloomed = 1

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if self._bloomed == 0:
            print(f" {self.get_name().capitalize()} has not bloomed yet")
        if self._bloomed == 1:
            print(f" {self.get_name().capitalize()} is blooming beautifully!")


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

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.get_name()} to produce shade]")
        if self.get_height() > 0 and self.get_trunk_diameter() > 0:
            print(
                f"Tree {self.get_name().capitalize()} now produces a shade of "
                f"{round(self.get_height(), 1):.1f}cm long and "
                f"{round(self.get_trunk_diameter(), 1):.1f}cm wide."
            )
        else:
            print(f"{self.get_name().capitalize()} can't produce shade!")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.get_trunk_diameter(), 1):.1f}cm")


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
        print(f"[make {self.get_name()} grow and age for {days} days]")
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

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> float:
        return self._nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.get_harvest_season()}")
        print(f" Nutritional value: {int(self.get_nutritional_value())}")


def main() -> None:
    f = Flower("rose", 15, 10, "red", 0.1)
    t = Tree("oak", 200, 365, 0.8, 5)
    v = Vegetable("tomato", 5.0, 10, 2.1, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    f.show()
    print(f"[asking the {f.get_name()} to bloom]")
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
