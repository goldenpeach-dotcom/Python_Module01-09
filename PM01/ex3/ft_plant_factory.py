#!/usr/bin/env python3

class Plant:
    def __init__(
        self, name: str, height: float, days: int, growth_rate: float
        ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(
    f"Created: {self.name.capitalize()}: {round(self.height, 1)}cm, "
    f"{self.days} days old"
)

garden = [
    Plant("rose", 25.0, 30, 0.8),
    Plant("oak", 200.0, 365, 2.5),
    Plant("cactus", 5.0, 90, 0.1),
    Plant("sunflower", 80.0, 40, 2.5),
    Plant("fern", 15.0, 120, 0.2),
]


print("=== Plant Factory Output ===")
for g in garden:
    g.show()

# for g in garden:
#     g.show() リストの中身一つ一つにメソッドshow()を呼んでいる
# 	garden.show()✖リスト自体にメソッドを呼んではいけない
# gardenは値が入った箱であって、Plantそのものではない