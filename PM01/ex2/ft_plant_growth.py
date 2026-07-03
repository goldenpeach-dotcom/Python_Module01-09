class Plant:
    def __init__(self, n: str, h: float, days: int, g_rate: float) -> None:
        self.n = n
        self.h = h
        self.days = days
        self.g_rate = g_rate

    def grow(self) -> None:
        self.h += self.g_rate

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.n.title()}: {round(self.h, 1)}cm, {self.days} days old")


rose = Plant("rose", 25.0, 30, 0.8)


initial_height = rose.h

print("=== Garden Plant Growth ===")
rose.show()
for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age()
    rose.show()
growth = round(rose.h - initial_height, 1)
print(f"Growth this week: {growth}cm")
