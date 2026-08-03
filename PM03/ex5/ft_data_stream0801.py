import random
from typing import Generator

players = [
    "bob",
    "alice",
    "dylan",
    "charlie"
]

actions = [
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
        list_remain = random.choice(events_list)
        events_list.remove(list_remain)
        yield list_remain


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()

    for index in range(3):
        event = next(gen)
        print(f"Event {index} : Player {event[0]} did action {event[1]}")

    events_list = []

    for element in range(10):
        event = next(gen)
        events_list.append(event)
    print(f"Built list of 10 events:{events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
