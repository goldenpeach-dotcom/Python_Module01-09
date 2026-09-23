from typing import Literal, List, Dict
from functools import reduce
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

def main() -> None:

    spells:List[int] = [40, 40, 20]
    print("Testing spell reducer...")
    sr_add: int = spell_reducer(spells, "add")
    sr_mul: int = spell_reducer(spells, "multiply")
    sr_max: int = spell_reducer(spells, "max")

    print(" Sum:", sr_add)
    print(" Product:", f"{sr_mul * 7.5:.0f}")
    print(" Max:", sr_max)

if __name__ == "__main__":
    main()
