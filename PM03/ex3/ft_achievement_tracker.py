import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer"
    "Untouchable"
]


def gen_player_achievements() -> set[str]:
    num: int = random.randint(1, len(ACHIEVEMENTS))
    return set(random.sample(ACHIEVEMENTS, k=num))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    p1: set[str] = gen_player_achievements()
    p2: set[str] = gen_player_achievements()
    p3: set[str] = gen_player_achievements()
    p4: set[str] = gen_player_achievements()
    print(f"Player Alice  : {p1}")
    print(f"Player Bob    : {p2}")
    print(f"Player Charlie: {p3}")
    print(f"Player Dylan  : {p4}")
    print()
    print(f"All distinct achievements: {p1.union(p2, p3, p4)}\n")
    print(f"Common achievements: {p1.intersection(p2, p3, p4)}\n")
    print(f"Only Alice has  : {p1.difference(p2.union(p3, p4))}")
    print(f"Only Bob has    : {p2.difference(p3.union(p4, p1))}")
    print(f"Only Charlie has: {p3.difference(p4.union(p1, p2))}")
    print(f"Only Dylan has  : {p4.difference(p1.union(p2, p3))}\n")
    print(f"Alice is missing  : {set(ACHIEVEMENTS).difference(p1)}")
    print(f"Bob is missing    : {set(ACHIEVEMENTS).difference(p2)}")
    print(f"Charlie is missing: {set(ACHIEVEMENTS).difference(p3)}")
    print(f"Dylan is missing  : {set(ACHIEVEMENTS).difference(p4)}")


if __name__ == "__main__":
    main()