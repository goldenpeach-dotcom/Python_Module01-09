import sys

def count_argv(args_lst: list[str]) -> None:
    if(len(args_lst) < 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args_lst[0:])}")
        i: int = 0
        while i < len(args_lst):
            print(f"Argument {i + 1}: {args_lst[i]}")
            i += 1
    print(f"Total arguments: {len(args_lst) + 1}")

def main() -> None:
    print("=== Command Quest ===")
    program_name, *args = sys.argv
    print(f"Program name: {program_name}")
    count_argv(args)


if __name__ == "__main__":
    main()