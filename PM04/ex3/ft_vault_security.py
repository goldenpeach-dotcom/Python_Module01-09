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
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    res: tuple[bool, str] = secure_archive("/not/existing/file", "r", "")
    print(res)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    res = secure_archive("etc/master.passwd", "r", "")
    print(res)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    res = secure_archive("ancient_fragment.txt", "r", "")
    print(res)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    if res[0]:
        previous_content = res[1]
        res = secure_archive("test.txt", "w", previous_content)
        print(res)
    else:
        print("Skipped writing because loading failed")


if __name__ == "__main__":
    main()
