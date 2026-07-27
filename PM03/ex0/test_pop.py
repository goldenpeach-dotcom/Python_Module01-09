import sys

def count_argv(args_lst: list[str]) -> None:
    if(len(args_lst) < 2):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args_lst[0:])}")
        i: int = 1
        while i < len(args_lst):
            print(f"Argument {i}: {args_lst[i]}")
            i += 1
    print(f"Total arguments: {len(args_lst) + 1}")

def main() -> None:
    print("=== Command Quest ===")
    argv_copy = sys.argv.copy()
    program_name = argv_copy.pop(0)
    print(f"Program name: {program_name}")
    count_argv(argv_copy)


if __name__ == "__main__":
    main()