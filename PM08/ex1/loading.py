#!/usr/bin/env python3
"""
Exercise 1 — loading.py
Matrix Data Loading Program
"""

import sys
import importlib
from typing import Tuple, Optional, Any


# ------------------------------------------------------------
# 依存関係チェック
# ------------------------------------------------------------
def check_dependency(name: str, description: str) -> Optional[Any]:
    """
    指定されたモジュールを import し、バージョンを表示する。
    見つからない場合は None を返す。
    """
    try:
        module = importlib.import_module(name)
        # バージョンはトップレベル matplotlib から取る
        if name == "matplotlib.pyplot":
            import matplotlib
            version = matplotlib.__version__
            display_name = "matplotlib"
        else:
            version = module.__version__
            display_name = name
        print(f"[OK] {display_name} ({version}) - {description}")
        return module
    except Exception:
        print(f"[MISSING] {name} - install with pip or poetry")
        return None


# ------------------------------------------------------------
# numpy によるデータ生成
# ------------------------------------------------------------
def generate_matrix_data(np_module) -> Any:
    """
    PDF要件：
    - データソースは numpy のみ
    - range() や手書きリストは禁止
    """
    return np_module.random.randn(1000)


# ------------------------------------------------------------
# pandas による分析
# ------------------------------------------------------------
def analyze_data(pd_module: Any, data: Any) -> Tuple[Any, Any]:
    # numpy の配列を表形式に変換
    df = pd_module.DataFrame({"values": data})
    summary = df.describe()
    return df, summary


# ------------------------------------------------------------
# matplotlib による可視化
# ------------------------------------------------------------
def visualize(plt_module, df) -> None:
    fig = plt_module.figure(figsize=(8, 4))
    df["values"].plot(kind="line")
    plt_module.title("Matrix Data Analysis")
    fig.savefig("matrix_analysis.png")


# ------------------------------------------------------------
# pip と Poetry の違いを示す補助表示
# ------------------------------------------------------------
def show_dependency_instructions() -> None:
    print("\nDependency installation instructions:")
    print("pip:    pip install -r requirements.txt")
    print("Poetry: poetry install\n")


# ------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------
def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas = check_dependency("pandas", "Data manipulation ready")
    numpy = check_dependency("numpy", "Numerical computation ready")
    requests = check_dependency("requests", "Network access ready")
    matplotlib = check_dependency("matplotlib.pyplot", "Visualization ready")

    # 必須依存が欠けていたら終了
    if not (pandas and numpy and matplotlib):
        print("\nERROR: Missing dependencies.")
        show_dependency_instructions()
        return

    print("Analyzing Matrix data...")
    data = generate_matrix_data(numpy)
    print(f"Processing {len(data)} data points...")

    df, summary = analyze_data(pandas, data)

    print("Generating visualization...")
    visualize(matplotlib, df)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
