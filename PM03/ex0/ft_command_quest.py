#!/usr/bin/env python3
import sys


def count_argv(args_lst: list[str]) -> None:
    if len(args_lst) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args_lst[1:])}")
        i: int = 1
        while i < len(args_lst):
            print(f"Argument {i}: {args_lst[i]}")
            i += 1
    print(f"Total arguments: {len(args_lst)}")


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    count_argv(sys.argv)


if __name__ == "__main__":
    main()
