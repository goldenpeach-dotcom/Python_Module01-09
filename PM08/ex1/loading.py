#!/usr/bin/env python3
"""
Exercise 1 — loading.py
Matrix Data Loading Program
"""

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
def generate_matrix_data(np_module: Any) -> Any:
    """
    PDF要件：
    - データソースは numpy のみ
    - range() や手書きリストは禁止
    """
    return np_module.random.randn(1000)


# ------------------------------------------------------------
# requestsで外部APIからデータを取得
# ------------------------------------------------------------
def fetch_matrix_data(
    requests_module: Any,
    np_module: Any
    ) -> Any:
    """
    PDF要件：
    - 外部APIから実データを取得する場合はrequestsを使用
    - random.org APIから真の乱数を取得してnumpy配列に変換
    """
    try:
        url = (
            "https://www.random.org/integers/?num=1000&min=-100"
            "&max=100&col=1&base=10&format=plain"
        )
        response = requests_module.get(url)
        response.raise_for_status()
        lines = response.text.strip().split("\n")
        data = np_module.array(lines, dtype=float)
        return data
    except requests_module.exceptions.HTTPError as e:
        print(f"[ERROR] API request failed: {e}")
        return None
    except requests_module.exceptions.RequestException as e:
        print(f"[ERROR] Network error: {e}")
        return None


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
def visualize(plt_module: Any, df: Any) -> None:
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
# データをロードする関数
# ------------------------------------------------------------
def load_data(source: str, numpy: Any, requests: Any | None=None) -> Any:
    if source == "numpy":
        return generate_matrix_data(numpy)

    if source == "api":
        if requests is None:
            print("[WARNING] requests missing — falling back to numpy")
            return generate_matrix_data(numpy)
        return fetch_matrix_data(requests, numpy)

    raise ValueError(f"Unknown data source: {source}")


# ------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------
def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas = check_dependency("pandas", "Data manipulation ready")
    numpy = check_dependency("numpy", "Numerical computation ready")
    matplotlib = check_dependency("matplotlib.pyplot", "Visualization ready")

    use_api: bool = True  # or False

    if use_api:
        requests = check_dependency("requests", "Network access ready")
    else:
        requests = None

    # 必須依存が欠けていたら終了
    if not (pandas and numpy and matplotlib):
        print("\nERROR: Missing dependencies.")
        show_dependency_instructions()
        return

    print("Analyzing Matrix data...")
    source = "api"  # or "numpy"
    data = load_data(source, numpy, requests)
    if data is None:
        raise ValueError("No data was loaded")

    print(f"Processing {len(data)} data points...")

    df, summary = analyze_data(pandas, data)

    print("Generating visualization...")
    visualize(matplotlib, df)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
