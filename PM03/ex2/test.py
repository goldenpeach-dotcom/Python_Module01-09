def try_parse_coordinates(text: str) -> tuple[float, float, float] | None:
    coordinates = text.split(",")
    if len(coordinates) != 3:
        print("Invalid syntax")
        return None
    try:
        values = [float(c.strip()) for c in coordinates]
    except ValueError as e:
        print(f"Error: {e}")
        return None
    return (values[0], values[1], values[2])


def get_player_pos() -> tuple[float, float, float]:
    result = None
    while result is None:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        result = try_parse_coordinates(text)
    return result

# 座標を入力させる場面の別バージョン（while Trueを使わなかったら）
# 入力を一回受け取って検証するtry_parse_coordinates
# 成功するまで繰り返すget_player_pos()