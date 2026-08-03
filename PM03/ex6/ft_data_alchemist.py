import random


def main() -> None:
    players: list[str] = ["bob", "alice", "Dylan", "charlie"]

    capitalized_players: list[str] = [name.capitalize() for name in players]

    capitalized_only: list[str] = [
        name for name in players if name[0].isupper()
    ]

    scores: dict[str, int] = {
        name: random.randint(50, 100) for name in capitalized_players
    }

    total_players = len(scores)
    average_score: float = (
        sum(scores.values()) / total_players if total_players > 0 else 0.0
    )
    high_scores: dict[str, int] = {
        name: score
        for name, score in scores.items()
        if score > average_score
    }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {capitalized_only}")
    print(f"Score dict: {scores}")
    print(f"Score average is {average_score:.1f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
