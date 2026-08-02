import random


def main() -> None:
    players: list[str] = ["bob", "alice", "Dylan", "charlie"]

    capitalized_players: list[str] = [name.capitalize() for name in players]

    capitalized_only: list[str] = [name for name in players if name[0].isupper()]

    scores: dict[str, int] = {name: random.randint(50, 100) for name in capitalized_players}

    average_score: float = sum(scores.values()) / len(scores)
    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average_score}

    print("=== Game Data Alchemist ===\n")
    print("Initial list of players: ", players)
    print("New list with all names capitalized: ", capitalized_players)
    print("New list of capitalized names only: ", capitalized_only)
    print("Score dict:", scores)
    print("Score average is ", average_score)
    print("High scores: ", high_scores)


if __name__ == "__main__":
    main()