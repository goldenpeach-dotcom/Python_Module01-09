import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        coordinates = user_input.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        try:
            values = [float(coord.strip()) for coord in coordinates]
            x, y, z = values
            return (x, y, z)
        except ValueError:
            print(
                f"Error on parameter '{user_input}': "
                f"could not convert string to float: '{user_input}'"
            )
            continue


def main() -> None:
    print("=== Game Coordinate System ===")

    x1, y1, z1 = get_player_pos()

    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_to_center = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)

    print(f"Distance to center: {distance_to_center}\n")

    print("Get a second set of coordinates")

    x2, y2, z2 = get_player_pos()
    distance_between_2coords = round(
        math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4
        )

    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance_between_2coords}\n"
    )


if __name__ == "__main__":
    main()
