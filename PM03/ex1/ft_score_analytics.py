#!/usr/bin/env python3
import sys


class ArgcError(Exception):
    def __init__(self, message="No score provided!") -> None:
        super().__init__(message)


class ScoreError(Exception):
    def __init__(self, message="No score provided!") -> None:
        super().__init__(message)


def is_valid_score(s: str) -> bool:
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()


def check_scores(args_lst: list[str]) -> None:
    if len(args_lst) < 2:
        raise ScoreError()

    invalid: list[str] = []
    for s in args_lst[1:]:
        if not is_valid_score(s):
            invalid.append(s)

    if invalid:
        lines = [f"Invalid parameter: {s}" for s in invalid]
        raise ArgcError("\n".join(lines))


def analytics_print(args_lst: list[str]) -> None:
    program_name, *args = args_lst
    scores = [int(a) for a in args]
    print(f"Scores processed: {scores}")
    print(f"Total players   : {len(scores)}")
    print(f"Total scores    : {sum(scores)}")
    print(f"Average Scores  : {sum(scores) / len(scores)}")
    print(f"High score      : {max(scores)}")
    print(f"Low score       : {min(scores)}")
    print(f"Score range     : {max(scores) - min(scores)}")


def analytics_argv(args_lst: list[str]) -> None:
    usage = (
        "No score provided. "
        f"Usage: {args_lst[0]} <score1> <score2> ..."
    )
    try:
        check_scores(args_lst)
        analytics_print(args_lst)
    except ArgcError as e:
        print(e)
        print(usage)
    except ScoreError:
        print(usage)


def main() -> None:
    print("=== Player Score Analytics ===")
    analytics_argv(sys.argv)


if __name__ == "__main__":
    main()
