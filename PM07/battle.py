from ex0.factories import FlameFactory, AquaFactory
from ex0.factories.creature_factory import CreatureFactory

# test the ex0
# Instantiate the Flameling and Aquabub factories
# Use a singgle function that receives a factory object and verifies that it can create the base and evevolved Creature ,and then each Creature can be described and can attack
# Another function that receives both factories and makes base Creature fight

def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory):
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(creature1.describe())
    print(" vs. ")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())

def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()