#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.days} days old"
        )


def main() -> None:
    garden = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ===")
    for p in garden:
        p.show()


if __name__ == '__main__':
    main()
