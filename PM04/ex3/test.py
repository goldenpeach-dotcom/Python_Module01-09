# 自分でコンテキストマネージャを作ってみる。

class MyFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("called __enter__: opening the file")
        self.f = open(self.name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        print("called__exit__: closing the file")
        print("exc_type", exc_type)
        print("exc_value", exc_value)
        print("traceback", traceback)
        self.f.close()
        # ここでFalseを返すと、例外はそのまま再送出される
        return False


with MyFile("test.txt", "w") as f:
    print("in with block")
    f.write("hello")