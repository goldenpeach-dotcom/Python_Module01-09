def input_temparature(temp_str: str) -> int:
    if temp_str is None:
        raise ValueError("temp_str must not be None")
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")  
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temparature() -> None:
    for vals in ["100", "-50", None]:
        try:
            print(f"Input data is '{vals}'")
            temp_valid = input_temparature(vals)
            print(f"Temparature is now {temp_valid}°C")
        except (ValueError, TypeError) as e:
            print(f"Caught input_temparature error: {e}")

if __name__ == "__main__":
    print("=== Garden Temparature ===\n")
    test_temparature()

    print("All test completed - program didn't crash!\n")