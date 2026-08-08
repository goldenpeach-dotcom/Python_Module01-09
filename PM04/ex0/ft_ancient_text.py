#! /usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    f: typing.IO[str] | None = None

    try:
        f = open(file_name, "r")
        content: str = f.read()
        print("---\n")
        print(content)
        print("\n---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file {file_name}: {e}")
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")

if __name__ == "__main__":
    main()
