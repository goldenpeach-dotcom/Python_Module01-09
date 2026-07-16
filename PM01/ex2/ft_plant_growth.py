#!/usr/bin/env python3

class Plant:
    def __init__(
        self, name: str, height: float, days: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate
        self.initial_height = height

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, {self.days} days old"
        )


def main() -> None:
    rose = Plant("rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth = round(rose.height - rose.initial_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == '__main__':
    main()
