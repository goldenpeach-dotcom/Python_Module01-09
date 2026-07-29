class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def run_watering_test(plants: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)

    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    run_watering_test(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    run_watering_test(["Tomato", "lettuce", "Carrots"])

    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
