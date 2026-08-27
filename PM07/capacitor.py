from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex0.factories.creature_factory import CreatureFactory


def test_healingfactory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

def test_transformfactory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    test_healingfactory(heal)
    print()
    test_transformfactory(transform)


if __name__ == "__main__":
    main()
