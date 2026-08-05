import random

MIN_ACHIEVEMENTS: int = 3
MAX_ACHIEVEMENTS: int = 10

ACHIEVEMENTS: set[str] = {
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
    "Sharp Mind",
    "Boss Slayer",
    "Untouchable",
}


def gen_player_achievements() -> set[str]:
    achievements_number: int = random.randint(
        MIN_ACHIEVEMENTS, MAX_ACHIEVEMENTS
        )
    player_achievements: set[str] = set(
        random.sample(list(ACHIEVEMENTS), achievements_number)
        )
    return player_achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, ach in players.items():
        print(f"{name:8}: {ach}")
    print()

    all_unique: set[str] = set.union(*players.values())
    print(f"All distinct achievements: {all_unique}\n")

    common: set[str] = set.intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, ach in players.items():
        others_union: set[str] = set.union(
            *(
                other_ach
                for other_name, other_ach in players.items()
                if other_name != name
            )
        )
        only_this: set[str] = ach.difference(others_union)
        print(f"Only {name:8} has: {only_this}")
    print()

    for name, ach in players.items():
        missing: set[str] = all_unique.difference(ach)
        print(f"{name:8} is missing: {missing}")
    print()


if __name__ == "__main__":
    main()
