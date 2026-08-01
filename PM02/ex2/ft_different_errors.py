def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("aaa")

    elif operation_number == 1:
        100 / 0

    elif operation_number == 2:
        open("test.txt")

    elif operation_number == 3:
        "aaa" + 100

    else:
        pass
    
    return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation_number in range(5):
        try:
            print(f"Testing operation {operation_number}...")
            garden_operations(operation_number)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")
        else:
            print("Operation completed successfully\n")
    print("All error types tested successfully!\n")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
