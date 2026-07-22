def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("aaa")

    elif operation_number == 1:
        100 / 0

    elif operation_number == 2:
        open("test.txt")

    elif operation_number == 3:
        "aaa" + 100

    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for operation_number in range(5):
        try:
            print(f"Testing operation {operation_number}...")
            garden_operations(operation_number)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")
        else:
            print("Operation completed successfully\n")
    print("All error types tested successfully!\n")


if __name__ == "__main__":
    test_error_types()

# ガーデンプログラムでは、さまざまな種類の問題が発生する可能性があります。Pythonには状況に応じたさまざ
# まな種類のエラーがあり、それらを個別に、あるいはまとめて捕捉することができます。
# 不具合のあるコードを含む関数 `garden_operations(operation_number)` を作成してください。0 から 3 までの
# `operation_number` の各値に対して、異なる不具合のあるコードが以下のいずれかの例外を発生させます:
# •ValueError - 不正なデータが渡された場合（例：int() に数値ではなく "abc" を渡した場合）
# •ZeroDivisionError - ゼロで除算しようとした場合
# •FileNotFoundError - 存在しないファイルを開こうとした場合（ファイルが開かれていない場合は、close()する必要はありません）
# •TypeError - 混在させることができない異なる型を混ぜようとした場合（文字列と数値を足そうとしません
# でしたか？）

# operation_numberのその他の値には不具合のあるコードは含まれておらず、単に処理を終了します。
# 以下の機能を持つ test_error_types() 関数を作成してください：
# •発生する各エラーの種類を表示する
# •各エラーを捕捉し、何が問題だったかを説明する
# •各エラー発生後もプログラムが実行を継続することを実証する