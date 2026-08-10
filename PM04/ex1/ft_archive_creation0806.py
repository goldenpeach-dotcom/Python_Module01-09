#! /usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    f: typing.IO[str] | None = None
    content: str = ""

    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print("---\n")
        print(content)
        print("\n---")
    except (
        OSError,
        UnicodeDecodeError
    ) as e:
        print(f"Error    opening file {file_name}: {e}")
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")

    # Transform data + #
    lines: list[str] = content.split("\n")
    archived_lines: list[str] = [
        line + "#"
        for line in lines
    ]
    new_content: str = "\n".join(archived_lines)

    print("Transform data:--")
    print(new_content)

    save_name: str = input(
        "Enter new file name(or empty): "
    )

    if save_name == "":
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{save_name}'")
        out: typing.IO[str] | None = None
        try:
            out = open(save_name, "w",encoding="utf-8")
            out.write(new_content)
            print(f"Data saved in file '{save_name}'.\n")
        except (OSError) as e:
            print(f"Error saving file '{save_name}': {e}")
        finally:
            if out is not None:
                out.close()


if __name__ == "__main__":
    main()
