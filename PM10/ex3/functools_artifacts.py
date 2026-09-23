from typing import Literal, List, Dict
from functools import reduce, partial, lru_cache
from collections.abc import Callable
import operator

# 呪文の威力を結合する。
def spell_reducer(
    spells:List[int],
    operation:Literal["add", "multiply", "max", "min"]
) -> int:

    """
    reduceを使って、spellsの威力を結合する。
    param:
        spells 呪文の威力
        operation add,multiply, max, minのいずれか
    return:
        計算結果の威力
    """
    if not spells:
        return 0

    ops: Dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    func: Callable[[int, int], int] = ops[operation]

    return reduce(func,spells)

# 基本の関数を受け取って、一部の値を固定して作った別の関数の辞書を返す
def enchant_items(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()}({power}) {target}"

def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> Dict[str, Callable[[str], str]]:
    """
        
        param:
            base_enchantment(power:int, element: str, target: str) -> str
        return:
           elementsを固定した新しい関数
    """
    if not callable(base_enchantment):
        raise TypeError("partial_enchanter needs an enchantment function")

    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")

    return{
        "fire": fire,
        "ice": ice,
        "lightning": lightning,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def main() -> None:
    spells:List[int] = [40, 40, 20]
    print("Testing spell reducer...")
    sr_add: int = spell_reducer(spells, "add")
    sr_mul: int = spell_reducer(spells, "multiply")
    sr_max: int = spell_reducer(spells, "max")

    print(" Sum:", sr_add)
    print(" Product:", f"{sr_mul * 7.5:.0f}")
    print(" Max:", sr_max)

    print("\nTesting partial enchanter...")
    ench: Dict[str,Callable[[str], str]] = partial_enchanter(enchant_items)
    print(ench["fire"]("Sword"))
    print(ench["ice"]("Shield"))
    print(ench["lightning"]("Bow"))

    print("\nTesting memoized fibonacci...")
    for number in (0, 1, 10, 15):
        print(f"fib({number}):", memoized_fibonacci(number))
    print("Cache:", memoized_fibonacci.cache_info())


if __name__ == "__main__":
    main()
