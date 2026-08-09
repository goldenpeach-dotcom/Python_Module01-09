#! /usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> str | None:
    f: typing.IO[str] | None = None
    content: str = ""

    try:
        f = open(file_name, "r")
        content = f.read()
        print("---\n")
        print(content)
        print("\n---")

    except (
        OSError,
        UnicodeDecodeError
    ) as e:
        print(
            f"[STDERR]Error opening file {file_name}: {e}",
            file=sys.stderr
        )
        return None
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")
    return content


def archive_content(content: str) -> str:
    lines: list[str] = content.split("\n")
    archived_lines: list[str] = [
        line + "#"
        for line in lines
    ]
    return "\n".join(archived_lines) + "\n"


def save_file(f_name: str, content: str) -> None:
    out: typing.IO[str] | None = None
    try:
        out = open(f_name, "w")
        out.write(content)
        print(f"Data saved in file '{f_name}'.")
    except OSError as e:
        print(f"Error saving file: '{f_name}': {e}")
        print("Data not saved.")
    finally:
        if out is not None:
            out.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    content: str | None = read_file(file_name)
    if content is None:
        return

    new_content: str = archive_content(content)
    print("Transform data:")
    print(new_content)

    print("Enter new file name(or empty): ", end="")
    sys.stdout.flush()
    save_name: str = sys.stdin.readline().rstrip("\n")

    if save_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{save_name}'")
    save_file(save_name, new_content)


if __name__ == "__main__":
    main()
