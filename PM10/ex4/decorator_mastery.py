from typing import Any
from collections.abc import Callable
from functools import wraps
import time
import inspect


# 関数の実行時間を測定するデコレーターを作る
def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    # wraps を使って関数名を保持する
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # 関数を実行する前に時間を記録
        start: float = time.time()
        # 元の関数を実行する
        result: Any = func(*args, **kwargs)
        # 関数を実行した後に時間を記録
        end: float = time.time()
        # 実行時間を print する
        print(f"{func.__name__} completed  in {end - start:.3f} seconds")
        # 元の関数の結果を返す
        return result
    return wrapper


# パワーレベルを検証するデコレータファクトリーを作成する。
# パラメータ化されたバリデーションデコレーター
def power_validator(
        min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # 関数のシグネチャを取得
            sig = inspect.signature(func)
            bound = sig.bind_partial(*args, **kwargs)
            bound.apply_defaults()

            # power 引数を名前で取得
            power = bound.arguments.get("power")

            # powerがみつからないときはそのまま実行
            if power is None:
                return func(*args, **kwargs)

            # バリデーション
            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


# リトライデコレーター
# 失敗した呪文を再試行するデコレーター
def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            # 全部失敗したら
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    def __init__(self) -> None:
        self.spells: dict[str, Callable[[int], str]] = {}

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return isinstance(name, str) and len(name) >= 3

    def register_spell(
        self,
        name: str,
        func: Callable[..., Any]
    ) -> None:
        self.spells[name] = func

    @retry_spell(3)
    @power_validator(10)
    @spell_timer
    def cast_spell(self, spell_name: str, power: int) -> str:
        if not self.validate_mage_name(spell_name):
            return "Invalid spell name"

        spell = self.spells.get(spell_name)

        if not spell:
            return "Unknowm spell"

        return spell(power)


def main() -> None:

    print("Testing spell timer...")
    print("Casting fireball...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        return "Fireball cast!"

    print("Result:", fireball("orc", 15))

    print("\nTestting retrying spell...")

    @retry_spell(3)
    def unstable_spell() -> None:
        raise ValueError("Boom!")

    print(unstable_spell())

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")

    guild = MageGuild()

    # validate_mage_nameのテスト
    print(guild.validate_mage_name("Lightning"))
    print(guild.validate_mage_name("Li"))
    # spellを登録
    guild.register_spell(
        "lightning",
        lambda power: f"Lightning strikes with {power} power!"
        )
    guild.register_spell(
        "heal",
        lambda power: f"Healing with {power} power!"
        )

    # 実行
    print(guild.cast_spell("lightning", 15))
    print(guild.cast_spell("heal", 5))
    # spell_timerは関数をデコレートするもの。
    # 関数を返すオブジェクトに属性アクセスしてはいけない
    #     st = spell_timer(fireball)
    #     print(f"Casting {st.func} ...")
    #     print(f"Spell completed in {st.time:.3f} seconds")
    #     print(f"Result: {st.func} cast!")

    #     print("\nTesting retrying spell...")
    #     rs = retry_spell(3)
    #     print("Waaaaaaagh spelled !")

    #     print("Testing MageGuild...")
    #     light = MageGuild.cast_spell(lightning("fireball", 15))
    #     healing = MageGuild.cast_spell(heal("lightning", 5))
    # except Exception as e:
    #     print("error!", e)


if __name__ == "__main__":
    main()
