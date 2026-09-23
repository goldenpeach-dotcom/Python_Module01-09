from collections.abc import Callable
from typing import Any

# カウントを行うクロージャを作成
def mage_counter() -> Callable[[], int]:
    count: int = 1
    def counter() -> int:
        nonlocal count
        current: int = count 
        count += 1
        return current
    return counter

# パワーの蓄積器を作成する。（どうやって前の値を憶えておくか？）
def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def accumulate(add_pwr: int) -> int:
        nonlocal power
        power += add_pwr
        return power

    return accumulate

# エンチャント関数の作成（指定されたエンチャントを適用する）
def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


# # メモリ管理システムの作成'store'関数(key,value)を受け取りその記憶を保持
# # 'recall'関数keyを受け取り保存された値を返すかMemory not found
def memory_vault() -> dict[str, Callable[..., Any]]:
    storage: dict[str, Any] = {}

    def store(key: str, value: str) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    print("Testting maze counter...")
    counter_a = mage_counter()
    print(f" counter_a call 1: {counter_a()}")
    print(f" counter_a call 2: {counter_a()}")

    counter_b = mage_counter()
    print(f" counter_b call 1: {counter_b()}")

    print("Testting spell accumulator...")
    initial = 100
    acc = spell_accumulator(initial)

    print(f" Base {initial}, add 20: {acc(20)}")
    print(f" Base {initial}, add 30: {acc(30)}")

    print("Testting enchantment factory...")

    flame = enchantment_factory("Flaming")
    frozen = enchantment_factory("Flozen")

    print("", flame("Sword"))   # Flaming Sword
    print("", frozen("Shield"))    # Flozen Shield

    print("Testting memory vault...")
    vault = memory_vault()

    print(" Store 'secret' = 42")
    vault["store"]("secret", 42)

    print(f" Recall 'secret': {vault['recall']('secret')}")
    print(f" Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()