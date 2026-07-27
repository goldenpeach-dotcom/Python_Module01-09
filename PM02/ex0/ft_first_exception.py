def input_temparature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temparature() -> None:
    for vals in ["25", "abc", None]:
        try:
            print(f"Input data is '{vals}'")
            temp_valid = input_temparature(vals)
            print(f"Temparature is now {temp_valid}°C")
        except (ValueError, TypeError) as e:
            print(f"Caught input_temparature error: {e}")

def main() -> None:
    print("=== Garden Temparature ===\n")
    test_temparature()

    print("All test completed - program didn't crash!\n")


if __name__ == "__main__":
    main()

#     1. if __name__ == "__main__": 直下のコードは呼び出しにくい
# 今の書き方だと、test_temparature() の実行結果を後から他のスクリプトからimportして再利用する、ということができません。main()に切り出せば from ft_garden_analytics import main として呼び出せます。

# 2. mypyやflake8的にも綺麗
# if __name__ == "__main__": ブロックの中身が多くなると、ネストが深くなったり変数のスコープが分かりにくくなったりします。main()に切り出すことで、トップレベルのコードがシンプルになります。

# 3. 42の課題では実質デファクトスタンダード
# 複数の関数を持つスクリプトでは、main()を用意して最後にif __name__ == "__main__": main()とするのが一般的な書き方です。採点者・レビュアーにも読みやすいです。