class GardenError(Exception):
    default_message = "Unknown plant error"
    def __init__(self, message: str = None) -> None:
        if message is None:
            message = self.default_message
        super().__init__(message)

class PlantError(GardenError):
    default_message = "Unknown plant error"

class WaterError(GardenError):
    default_message = "Unknown water error"

def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError(" Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)
    print()
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)
    print()
    print("Testing catching all garden errors...")

    try:
        check_plant()
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        check_water()
    except GardenError as e:
        print("Caught GardenError:", e)

    print()
    print("All custom error types work correctly!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
