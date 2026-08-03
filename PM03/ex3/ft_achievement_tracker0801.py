import random

ACHIEVEMENTS = [
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
    "Boss Slayer",
    "Untouchable"
]


def gen_player_achievements() -> set[str]:
    achievements_number = random.randint(3, 7)
    player_achievements = set(random.sample(ACHIEVEMENTS, achievements_number))
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

    common = set.intersection(*players.values())
    print(f"Common achievements: {common}\n")

    # 各プレイヤーの「その人だけ」
    for name, ach in players.items():
        others_union = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others_union |= other_ach   # union の短縮記法
        only_this = ach - others_union
        print(f"Only {name:8} has: {only_this}")
    print()

    # 各プレイヤーの「足りない実績」
    for name, ach in players.items():
        missing = all_unique - ach
        print(f"{name:8} is missing: {missing}")
    print()


if __name__ == "__main__":
    main()
