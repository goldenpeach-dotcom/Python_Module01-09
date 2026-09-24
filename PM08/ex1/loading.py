#!/usr/bin/env python3
import sys
import importlib


def check_dependency(name: str, description: str) -> bool:
    """
        param:
            name module_name
            description module
        return:
            the module if import succeeds, False otherwise.

    """
    top_name = name.split(".")[0]
    try:
        importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - install with pip or poetry")
        return False

    version = getattr(sys.modules[top_name], "__version__", "unknown")

    print(f"[OK] {top_name} ({version}) - {description}")
    return True


def generate_matrix_data() -> list[float]:
    """
    Data generation using NumPy
    """
    import numpy as np

    data: list[float] = np.random.randn(1000).tolist()

    return data


def fetch_matrix_data() -> list[float] | None:
    """
    Fetch true random numbers from random.org using requests.
    """
    import requests

    url = (
        "https://www.random.org/integers/?num=1000&min=-100"
        "&max=100&col=1&base=10&format=plain"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return [float(x) for x in response.text.split()]
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] API request failed: {e}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network error: {e}")
    except ValueError as e:
        print(f"[ERROR] Invalid data received: {e}")
    return None


def analyze_data(data: list[float]) -> dict[str, float]:
    """
    Summarize the data with pandas.
    """
    import pandas as pd

    df = pd.DataFrame({"values": data})
    summary = df["values"].describe()
    return {str(key): float(value) for key, value in summary.items()}


def visualize(data: list[float]) -> None:
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(8, 4))
    plt.plot(data)
    plt.title("Matrix Data Analysis")
    fig.savefig("matrix_analysis.png")
    plt.close(fig)


def show_dependency_instructions() -> None:
    print("\nDependency installation instructions:")
    print("pip:    pip install -r requirements.txt")
    print("Poetry: poetry install\n")


def load_data(source: str) -> list[float]:
    if source == "numpy":
        return generate_matrix_data()

    if source == "api":
        data = fetch_matrix_data()
        if data is None:
            print("[WARNING] API failed — falling back to numpy")
            return generate_matrix_data()
        return data

    raise ValueError(f"Unknown data source: {source}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pd_ok = check_dependency("pandas", "Data manipulation ready")
    np_ok = check_dependency("numpy", "Numerical computation ready")
    plt_ok = check_dependency("matplotlib.pyplot", "Visualization ready")
    requests_ok = check_dependency("requests", "Network access ready")

    if not (pd_ok and np_ok and plt_ok):
        print("\nERROR: Missing dependencies.")
        show_dependency_instructions()
        return

    source = "api" if requests_ok else "numpy"
    if source == "numpy":
        print("\n[WARNING]: requests missing - falling back to numpy")

    print("Analyzing Matrix data...")
    data = load_data(source)

    print(f"Processing {len(data)} data points...")
    summary = analyze_data(data)
    for key, value in summary.items():
        print(f"  {key}: {value:.3f}")

    print("Generating visualization...")
    visualize(data)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
