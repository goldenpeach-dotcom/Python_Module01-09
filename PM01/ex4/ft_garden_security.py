#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._height = 0.0
        self._days = 0

        if height < 0:
            print(f"{name.capitalize()}: Error, height can't be negative")
        elif height > 1000:
            print(f"{name.capitalize()}: Error, height can't be too big")
        else:
            self._height = height

        if days < 0:
            print(f"{name.capitalize()}: Error, age can't be negative")
        elif days > 1000:
            print(f"{name.capitalize()}: Error, age can't be too long")
        else:
            self._days = days

        print(
            f"Plant created: {self.name.capitalize()}: "
            f"{round(self._height, 1)}cm, {self._days} days old"
        )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def set_height(self, h: float) -> None:
        if h < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
            return
        elif h > 1000:
            print(f"{self.name.capitalize()}: Error, height can't be too big")
            print("Height update rejected")
            return
        else:
            self._height = float(h)
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, d: int) -> None:
        if d < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        elif d > 1000:
            print(f"{self.name.capitalize()}: Error, age can't be too long")
            print("Age update rejected")
            return
        else:
            self._days = d
            print(f"Age updated: {d} days")

    def show_current(self) -> None:
        print(
            f"Current state: {self.name.capitalize()}: {round(self._height, 1)}cm, "
            f"{self._days} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10, 0.8)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-3)
    rose.show_current()
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
