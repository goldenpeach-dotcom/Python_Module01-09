def input_temparature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if 0 <= temp_int and temp_int <= 40:  
        return temp_int
    else:
        return None

def test_temparature() -> None:
    for vals in ["25", "abc", None]:
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