from typing import Any

def input_temparature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def verify_and_print_temparature(val: Any) -> None:
    try:
        print(f"Input data is '{val}'")
        temp_valid = input_temparature(val)
        print(f"Temparature is now {temp_valid}°C")
    except(ValueError, TypeError) as e:
        print(f"Caught input_temparature error: {e}")


def test_temparature() -> None:
    verify_and_print_temparature("25")
    verify_and_print_temparature("abc")


def main() -> None:
    print("=== Garden Temparature ===\n")
    test_temparature()

    print("All test completed - program didn't crash!\n")


if __name__ == "__main__":
    main()
