import sys


def parse_arg(arg: str) -> tuple[str, int]:
    if ":" not in arg:
        raise ValueError(f"Error - invalid parameter '{arg}'")

    name, count_str = arg.split(":", 1)

    if not name:
        raise ValueError(f"Item name is empty: {arg}")

    try:
        count = int(count_str)
    except ValueError as e:
        raise ValueError(f"Quantity error for '{name}': {e}")

    return name, count


def calc_total(inventory: dict[str, int]) -> int:
    return sum(inventory.values())


def get_value(item: tuple[str, int]) -> int:
    return item[1]


def find_max_item(inventory: dict[str, int]) -> tuple[str, int]:
    return max(inventory.items(), key=get_value)


def find_min_item(inventory: dict[str, int]) -> tuple[str, int]:
    return min(inventory.items(), key=get_value)


def add_item(inventory: dict[str, int], name: str, count: int) -> None:
    if name in inventory:
        raise ValueError(f"Item already exists: {name}")
    inventory[name] = count


def calc_percentage(inventory: dict[str, int]) -> dict[str, float]:
    total = sum(inventory.values())
    if total == 0:
        return {name: 0.0 for name in inventory}

    percentages = {}
    for name, count in inventory.items():
        percentages[name] = (count / total) * 100

    return percentages


def display_percentages(percentages: dict[str, float]) -> None:
    for nm, pct in percentages.items():
        print(
            f"Item {nm} represents "
            f"{pct: .1f}%"
        )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    if len(sys.argv) == 1:
        print("Inventory is empty.")
        return

    for arg in sys.argv[1:]:
        try:
            name, count = parse_arg(arg)

            if name in inventory:
                print(f"Rebundant item '{name}' - discarding")
                continue

            inventory[name] = count

        except ValueError as e:
            print(e)
            continue

    if not inventory:
        print("no valid inventory items found.")
        return

    print("Got inventory: ", inventory)


    print("Item list : ", list(inventory))

    total = calc_total(inventory)
    print("Total items:", total)

    max_item = find_max_item(inventory)
    print("Most abundant:", max_item)

    min_item = find_min_item(inventory)
    print("Least abundant:", min_item)

    percentages = calc_percentage(inventory)
    display_percentages(percentages)

    add_item(inventory, "elixir", 3)
    print("After adding elixir:", inventory)


if __name__ == "__main__":
    main()
