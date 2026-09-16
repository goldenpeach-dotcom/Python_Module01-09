import sys
import os
import site

def is_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    return False

def get_env_name() -> str:
    # 1. 実行中の Python のフルパスを取る
    exe_path: str = sys.executable
    # 例: /home/.../PM08/matrix_env/bin/python3

    # 2. その一つ上のディレクトリを取る（bin）
    bin_dir: str = os.path.dirname(exe_path)
    # 例: /home/.../PM08/matrix_env/bin

    # 3. さらにその一つ上のディレクトリを取る（matrix_env）
    venv_root: str = os.path.dirname(bin_dir)
    # 例: /home/.../PM08/matrix_env

    # 4. 最後にそのディレクトリ名だけ取り出す
    env_name: str = os.path.basename(venv_root)
    # 例: matrix_env
    # 1行で書くと
    # venv_root = os.path.dirname(os.path.dirname(sys.executable))
    # return os.path.basename(venv_root)
    return env_name

def print_outside_venv() -> None:
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
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {virtual_environment}")
    print("")
    print(f"{message}")

def print_inside_matrix() -> None:
    virtual_environment: str = get_env_name()
    message: str = (
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n\n"
        "Package installation path:\n"
        f"{site.getsitepackages()[0]}"
    )
    print(f"MATRIX STATUS: Welcome to construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {virtual_environment}")
    print("")
    print(f"{message}")

def main() -> None:
    if is_venv():
        print_inside_matrix()
    else:
        print_outside_venv()


if __name__=="__main__":
    main()
