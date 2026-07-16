#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def show(self) -> None:
    print(
        f"{self.name.capitalize()}: "
        f"{self.height}cm, {self.days} days old"
    )


def main() -> None:
    garden = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 40),
        Plant("cactus", 15, 20),
    ]
    print("=== Garden Plant Registry ===")
    for p in garden:
        p.show()


if __name__ == '__main__':
    main()


# for 変数名 in　中身を一つずつ取り出せるもの
#     処理
# 変数名はclassと被らないよう注意
# garden = [リストの中には値だけしか書けない。]
# plant1 = Plant("rose", 25, 30)
# plant2 = Plant("sunflower", 80, 40)
# plant3 = Plant("cactus", 15, 20)
# 〇garden =  [plant1, plant2, plant3]→個別の変数名でアクセスできる
# 〇garden =  [
# 	Plant("rose", 25, 30)
# 	Plant("sunflower", 80, 40)
# 	Plant("cactus", 15, 20)
# ]　　　　　　　　　　　　　　　　　　　→インデックスgarden[0]のみアクセス可
# ✖garden = [
# 	plant1 = Plant("rose", 25, 30)
#     plant2 = Plant("sunflower", 80, 40)
#     plant3 = Plant("cactus", 15, 20)
# ]式を入れないこと
