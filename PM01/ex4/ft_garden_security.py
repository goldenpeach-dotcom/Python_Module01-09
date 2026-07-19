#!/usr/bin/env python3

DEFAULT_HEIGHT = 0.0
DEFAULT_AGE = 0

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float
    ) -> None:
        self._name = name
        self._growth_rate = growth_rate
        self._height = DEFAULT_HEIGHT
        self.set_height(height, is_init=True)
        self._days = DEFAULT_AGE
        self.set_age(days, is_init=True)

        print(
            f"Plant created: {self._name.capitalize()}: "
            f"{round(self._height, 1)}cm, {self._days} days old"
        )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, h: float, is_init: bool=False) -> None:
        if h < 0:
            print(f"{self._name.title()}: Error, height can't be negative")
            if not is_init:
                print("Height update rejected")
            return
        elif h > 1000:
            print(f"{self._name.title()}: Error, height can't be too big")
            if not is_init:
                print("Height update rejected")
            return
        self._height = float(h)
        if not is_init:
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, d: int,is_init: bool=False) -> None:
        if d < 0:
            print(f"{self._name.title()}: Error, age can't be negative")
            if not is_init:
                print("Age update rejected")
            return
        elif d > 1000:
            print(f"{self._name.title()}: Error, age can't be too long")
            if not is_init:
                print("Age update rejected")
            return
        self._days = d
        if not is_init:
            print(f"Age updated: {d} days")

    def show_current(self) -> None:
        print(
            f"Current state: {self._name.capitalize()}: "
            f"{round(self._height, 1)}cm, "
            f"{self._days} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10, 0.8)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-3)
    print()

    rose.show_current()


if __name__ == "__main__":
    main()
    # name = input("名前を入力してください: ")
    # height = float(input("高さ(cm)を入力してください: "))
    # age = int(input("日数を入力してください: "))

    # g = Plant(name, height, age)

    # new_height = float(input("新しい高さを入力してください: "))
    # g.get_height(new_height)

    # new_age = int(input("新しい日数を入力してください: "))
    # g.get_age(new_age)
# 今回は入力を求める課題ではなく自分でデータを用意する。

# こうすれば、実行するたびにユーザーが入力した値で set_height / set_age が呼ばれます。
# 整理すると
# 目的書き方最初のPlant作成時の値だけ入力させたい
# Plant(name, height, age) の3つだけinput()で受け取る（最初の回答の書き方）
# 更新時の値も毎回入力させたい
# update_height() / update_age() に渡す数値もinput()で受け取る（今回の書き方）
# $> python3 ft_garden_security.py
# === Garden Security System ===
# Plant created: Rose: 15.0cm, 10 days old
# Height updated: 25cm
# Age updated: 30 days
# Rose: Error, height can't be negative
# Height update rejected
# Rose: Error, age can't be negative
# Age update rejected
# Current state: Rose: 25.0cm, 30 days old
