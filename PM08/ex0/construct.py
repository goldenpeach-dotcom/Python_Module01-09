import sys
import os
import site

def main() -> None:
    # python3
    python_path: str = sys.executable
    # Virtual Environment
    virtual_environment: str = os.path.basename(
        os.path.dirname(os.path.dirname(python_path))
    ) 
    # Environment path
    venv_path: str = os.path.dirname(os.path.dirname(python_path))

    status: bool = False
    # 仮想環境にいるのかどうかチェックする。フラグ立てる？
    if sys.prefix != sys.base_prefix:
        status = True

    if status:
        install_path: str = site.getsitepackages()[0]
        stats_message: str = "Welcome to construct"
        message: str = (
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n\n"
            "Package installation path:\n"
            f"{install_path}"
        )
    else:
        stats_message: str = " You're still plugged in"
        virtual_environment = "None Detected"
        message = (
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            "To enter the construct, run:\n"
            "python-m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\Scripts\activate # On Windows\n"
            "Then run this program again."
        )


    print(f"MATRIX STATUS: {stats_message}")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {virtual_environment}")
    if status:
        print(f"Environment Path: {venv_path}")
    print("")
    print(f"{message}")


if __name__=="__main__":
    main()