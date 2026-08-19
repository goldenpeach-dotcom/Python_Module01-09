import random
from typing import Generator

players: list[str] = [
    "bob",
    "alice",
    "dylan",
    "charlie"
]

actions: list[str] = [
    "run",
    "eat",
    "move",
    "climb",
    "sleep",
    "release",
    "grab",
    "use"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)


def consume_event(
        events_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while events_list:
        idx = random.randrange(len(events_list))
        list_remain = events_list[idx]
        # [:] を左辺に付けることで「同じオブジェクトの中身をまるごと置き換える」
#         言語リファレンス(詳細な仕様)
# 6.3.4. スライス表記(Slicings) — [:] や [a:b] [a:b:c] の正式な文法・意味が定義されています
        events_list[:] = events_list[:idx] + events_list[idx+1:]
        # 元のコード
        # events_list = events_list.pop(0)
        yield list_remain


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()

    for index in range(1):
        event = next(gen)
        print(f"Event {index} : Player {event[0]} did action {event[1]}")

    events_list: list[tuple[str, str]] = []

    for element in range(10):
        event = next(gen)
        events_list.append(event)
    print(f"Built list of 10 events:{events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
