from types import TracebackType
from typing import IO, Literal, Optional, Type
# 自分でコンテキストマネージャを作ってみる。

class MyFile:
    def __init__(self, name: str, mode: Literal["r", "w", "a", "x"])-> None:
        self.name: str = name
        self.mode:Literal["r", "w", "a", "x"] = mode
        self.f: Optional[IO[str]] = None

    def __enter__(self) -> IO[str]:
        print("called __enter__: opening the file")
        self.f = open(self.name, self.mode)
        return self.f

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
        )-> Literal[False]:
        print("called__exit__: closing the file")
        print("exc_type", exc_type)
        print("exc_value", exc_value)
        print("traceback", traceback)
        if self.f is not None:
            self.f.close()
        # ここでFalseを返すと、例外はそのまま再送出される
        return False


with MyFile("test.txt", "w") as f:
    print("in with block")
    f.write("hello")