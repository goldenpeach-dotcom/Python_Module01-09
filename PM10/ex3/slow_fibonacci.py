from functools import lru_cache
import timeit

count = 0

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    global count
    count += 1

    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def slow_fibonacci(n: int) -> int:
    global count
    count += 1

    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

def main() -> None:
    global count
    count = 0
    print("普通のfibonacci...")
    print(slow_fibonacci(20))
    print("関数呼び出し回数:", count)
    time1 = timeit.repeat(lambda: slow_fibonacci(20), number=10, repeat=5)
    print("fib(20)を10回実行するのにかかった秒数（最速）:", min(time1))
    print("e-05は-10の５乗（小数点を左へ５つ動かす）")

    count = 0
    memoized_fibonacci.cache_clear()
    print("\nメモ化を使ったfibonacci")
    print(memoized_fibonacci(20))
    print("関数呼び出し回数:", count)
    time2 = timeit.repeat(
    lambda: (memoized_fibonacci.cache_clear(), memoized_fibonacci(20)),
    number=10,
    repeat=5
    )
    print("fib(20)を10回実行するのにかかった秒数(最速):", min(time2))

if __name__ == "__main__":
    main()