class GardenError(Exception):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def check_plant():
    raise PlantError(" The tomato plant is wilting!")


def check_water():
    raise WaterError(" Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")

    try:
        check_plant()
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        check_water()
    except GardenError as e:
        print("Caught GardenError:", e)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
