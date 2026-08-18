from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.rank: int = 0
        self.data: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        self.processors.append(processor)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    break
            else:
                print(
                    f"DataStream error - "
                    f"Can't process item in stream: {item} "
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for processor in self.processors:
            print(
                f"{type(processor).__name__}: total "
                f"{processor.rank} items processed, "
                f"remaining {len(processor.data)} on processor"
            )


def main() -> None:
    print("=== Code Nexus- Data Stream ===")

    print("\nInitialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print()

    print("Registering Numeric Processor\n")

    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send five batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("")

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("")

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
