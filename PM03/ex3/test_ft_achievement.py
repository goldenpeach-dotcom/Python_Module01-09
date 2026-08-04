import random

ACHIEVEMENTS = {
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
    achievements_number = random.randint(3, 10)
    player_achievements = set(
        random.sample(list(ACHIEVEMENTS), achievements_number)
        )
    return player_achievements


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, ach in players.items():
        print(f"{name:8}: {ach}")
    print()

    all_unique = set.union(*players.values())
    print(f"All distinct achievements: {all_unique}\n")

    all = set(ACHIEVEMENTS)
    nothin = all.difference(*players.values())
    print(f"nothin is: {nothin}\n" )
    common = set.intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, ach in players.items():
        others_union = set.union(
            *(ach for k, ach in players.items() if k != name)
            )
        only_this = ach.difference(others_union)
        print(f"Only {name:8} has: {only_this}")
    print()


    for name, ach in players.items():
        missing = all_unique.difference(ach)
        print(f"{name:8} is missing: {missing}")
    print()


if __name__ == "__main__":
    main()
