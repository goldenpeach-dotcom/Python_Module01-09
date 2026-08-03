 
#!/usr/bin/env python3
import sys


def set_inventory(args: list[str], inventory: dict[str, int]) -> bool:
    for arg in args:
        try:
            item_name, arg_quantity = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        else:
            try:
                quantity = int(arg_quantity)
            except ValueError as e:
                print(f"Quantity error for '{item_name}': {e}")
                continue
            inventory[item_name] = quantity
    if inventory == {}:
        print(
            "No items provided. Usage: python3 "
            "ft_inventory_system.py <item_name>:<quantity> ..."
        )
        return False
    return True


def show_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total_items: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_items}")
    if total_items != 0:
        for item in inventory.keys():
            ratio = inventory[item] / total_items
            print(f"Item {item} represents {round((ratio * 100), 1)}%")
    else:
        print("Error: Division by zero is not possible.")
    max_value = max(list(inventory.values()))
    min_value = min(list(inventory.values()))
    max_item = [k for k, v in inventory.items() if v == max_value][0]
    min_item = [k for k, v in inventory.items() if v == min_value][0]
    print(f"Item most abundant: {max_item} with quantity {max_value}")
    print(f"Item least abundant: {min_item} with quantity {min_value}")def merge_inventory(
    inventory: dict[str, int], new_item: dict[str, int]
) -> None:
    inventory.update(new_item)


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    if set_inventory(args, inventory) is False:
        return None
    show_inventory(inventory)
    new_item = {"magic_item": 1}
    merge_inventory(inventory, new_item)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()