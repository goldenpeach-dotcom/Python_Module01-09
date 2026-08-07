def secure_archive(
    file_name: str,
    operation: str,
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
            return (True, str(content))
        else:
            return(False,)
    except OSError as e:
        return (False, str(e))