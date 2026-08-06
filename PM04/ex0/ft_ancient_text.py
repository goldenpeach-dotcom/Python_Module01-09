import sys
import typing

# def get_file_name(args_lst: list[str]) -> str:
#     if len(args_lst) < 2:
#         print("Usage: ft_ancient_text.py <file>")
#         return None

#     try:
#         file_name: str = args_lst[1]
#         print(f"Accessing file '{file_name}'")
#         return file_name

#     except (ValueError, TypeError, IndexError) as e:
#         print(f"Usage: {args_lst[0]} <file> {e}")
#         return None


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        f: typing.IO[str] = open(file_name, "r")
    except(FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error opening file {file_name}: {e}")
        return

    content: str = f.read()

    print("---\n")
    print(content)
    print("\n---")

    f.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
