def input_temparature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temparature() -> None:
    for vals in ["25", "abc", None]:
        try:
            print(f"Input data is '{vals}'")
            temp_valid = input_temparature(vals)
            print(f"Temparature is now {temp_valid}°C")
        except Exception as e:
            print(f"Caught input_temparature error: {e}")
# - 手軽で確実、どんなエラーが来ても対応できる
# - ただし「具体的に何のエラーを想定しているか」が読み手に伝わりにくい

if __name__ == "__main__":
    print("=== Garden Temparature ===\n")
    test_temparature()

    print("All test completed - program didn't crash!\n")