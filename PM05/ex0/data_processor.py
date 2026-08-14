from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.rank: int = 0
        self.data: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data available to extract")
        return self.data.pop(0)

    def count_rank(self) -> int:
        current_rank = self.rank
        self.rank += 1
        return current_rank


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    # 引数の型ヒントを要件（単体またはリスト）に合わせ、戻り値は None にします
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            rank: int = self.count_rank()
            self.data.append((rank, str(item)))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper :text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            rank = self.count_rank()
            self.data.append((rank, item))


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:

        def is_valid_dict(d: Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            rank = self.count_rank()
            level = item.get("log_level", "")
            message = item.get("log_message", "")
            formatted_log = f"{level}: {message}"
            self.data.append((rank, formatted_log))


def main() -> None:
    # 1. Create instances for each specialized class.
    numeric: DataProcessor = NumericProcessor()
    text: DataProcessor = TextProcessor()
    log: DataProcessor = LogProcessor()

    print("=== Code Nexus - Data Processor ===\n")

    # =========================================================================
    # 2. Testing Numeric Processor
    # =========================================================================
    print("Testing Numeric Processor...")

    # Test valid and invalid data for each class through the validate method.
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    # Test at least one invalid data item with the ingest method
    # without prior validation,
    # and check that it raises an exception.
    # (This will leave a mypy warning on purpose)
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # mypy はここに
        # 「Argument 1 to "ingest" of "NumericProcessor"
        # has incompatible type "str"」
        # と警告を出します（意図通り）
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    # Ingest various data for each data processor
    # and then extract it using output.
    numeric_data = [1, 2, 3, 4, 5]
    # Ingest various data for each data processor
    # and then extract it 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)

    print("Extracting 3 values...")
    for i in range(3):
        rank, val = numeric.output()
        print(f"Numeric value {rank}: {val}")

    # =========================================================================
    # 3. Testing Text Processor
    # =========================================================================
    print("Testing Text Processor...")

    # Test valid and invalid data through validate
    print(f"Trying to validate input '42': {text.validate(42)}")

    # Ingest and extract
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")    # Test valid and invalid data for each class through the validate method.
    text.ingest(text_data)

    print("Extracting 1 value...")
    rank, val = text.output()
    print(f"Text value {rank}: {val}")

    # =========================================================================
    # 4. Testing Log Processor
    # =========================================================================
    print("Testing Log Processor...")

    # Test valid and invalid data through validate
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    # Ingest and extract
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)

    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log.output()
        print(f"Log entry {rank}: {val}")

    processors: list[DataProcessor] = [numeric, text, log]
    print("\n Polymorphism check[42]")
    for p in processors:
        print(type(p).__name__, "->", p.validate(42))

    try:
        print("抽象クラスのインスタンス化")
        dp = DataProcessor()
    except TypeError as e:
        print (f"TypeError!! {e}")
        return


if __name__ == "__main__":
    main()
