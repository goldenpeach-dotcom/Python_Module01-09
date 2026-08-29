from ex0 import CreatureFactory
from ex0 import FlameFactory
from ex0 import AquaFactory
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def test_tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            first, first_strategy = fighters[i]
            second, second_strategy = fighters[j]

            print()
            print("* Battle *")
            print(first.describe())
            print(" vs.")
            print(second.describe())
            print(" now fight!")

            try:
                messages = (
                    first_strategy.act(first) + second_strategy.act(second)
                )
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return

            for message in messages:
                print(message)


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    test_tournament([(flame, normal), (healing, defensive)])

    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    test_tournament([(flame, aggressive), (healing, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    test_tournament(
        [(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
