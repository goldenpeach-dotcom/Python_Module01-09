def secure_archive(
    file_name: str,
    operation: str = "r",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if operation == "r":
            with open(file_name, "r") as f:
                result = f.read()
            return (True, result)
        elif operation == "w":
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Mode error")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    res: tuple[bool, str] = secure_archive("/not/existing/file", "r", "")
    print(res)

    print("Using 'secure_archive' to read from an inaccessible file:")
    res = secure_archive("etc/master.passwd", "r", "")
    print(res)

    print("Using 'secure_archive' to read from a regular file:")
    res = secure_archive("ancient_fragment.txt", "r", "")
    print(res)

    print("Using 'secure_archive' to write previous content to a new file:")
    res = secure_archive(
        "test.txt", "w", "aaaaaaaaaaaaaaaaaaa"
        )
    print(res)

if __name__ == "__main__":
    main()
