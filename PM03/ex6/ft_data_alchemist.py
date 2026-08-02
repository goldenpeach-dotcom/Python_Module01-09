import random


def main() -> None:
    players = ["bob", "alice", "Dylan", "charlie"]

    capitalized_players = [name.capitalize() for name in players]

    capitalized_only = [name for name in players if name[0].isupper()]

    scores = {name: random.randint(50, 100) for name in capitalized_players}

    average_score = sum(scores.values()) / len(scores)
    high_scores = {
        name: score for name, score in scores.items() if score > average_score}

    print("=== Game Data Alchemist ===\n")
    print("Initial list of players: ", players)
    print("New list with all names capitalized: ", capitalized_players)
    print("New list of capitalized names only: ", capitalized_only)
    print("Score dict:", scores)
    print("Score average is ", average_score)
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()