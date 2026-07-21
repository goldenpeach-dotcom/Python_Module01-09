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

        print(
            f"Plant created: {self.get_name().capitalize()}: "
            f"{round(self.get_height(), 1)}cm, {self.get_age()} days old"
        )

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
                f"Error, height can't be negative"
            )
            if not is_init:
                print("Height update rejected")
            return
        elif h > 1000:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, height can't be too big"
            )
            if not is_init:
                print("Height update rejected")
            return
        self._height = float(h)
        if not is_init:
            print(f"Height updated: {int(self.get_height())}cm")

    def set_age(self, d: int, is_init: bool = False) -> None:
        if d < 0:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, age can't be negative"
            )
            if not is_init:
                print("Age update rejected")
            return
        elif d > 1000:
            print(
                f"{self.get_name().capitalize()}: "
                f"Error, age can't be too long"
            )
            if not is_init:
                print("Age update rejected")
            return
        self._days = d
        if not is_init:
            print(f"Age updated: {d} days")

    def show_current(self) -> None:
        print(
            f"Current state: {self.get_name().capitalize()}: "
            f"{round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10, 0.8)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-3)
    print()

    rose.show_current()


if __name__ == "__main__":
    main()
