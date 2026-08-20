#!/usr/bin/env python3
import sys


class ArgcError(Exception):
    def __init__(self, message: str = "No score provided!") -> None:
        super().__init__(message)


class ScoreError(Exception):
    def __init__(self, message: str = "Invalid score value!") -> None:
        super().__init__(message)


def check_scores(args_lst: list[str]) -> list[int]:
    if len(args_lst) < 2:
        raise ArgcError()

    valid: list[int] = []
    invalid: list[str] = []
    for s in args_lst[1:]:
        try:
            # valid.append(int(s))
            valid = valid + [int(s)]
        except ValueError:
            # invalid.append(s)
            invalid = invalid + [s]
            print(f"Invalid parameter: '{s}'")

    if not valid:
        raise ScoreError()

    return valid


def analytics_print(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players   : {len(scores)}")
    print(f"Total scores    : {sum(scores)}")
    print(f"Average scores  : {sum(scores) / len(scores):.1f}")
    print(f"High score      : {max(scores)}")
    print(f"Low score       : {min(scores)}")
    print(f"Score range     : {max(scores) - min(scores)}")


def analytics_argv(args_lst: list[str]) -> None:
    usage = f"Usage: {args_lst[0]} <score1><score2> ..."
    try:
        valid_scores = check_scores(args_lst)
        analytics_print(valid_scores)
    except ScoreError as e:
        print(e)
        print(f"No score provided! {usage}")
    except ArgcError as e:
        print(f"{e} {usage}")


def main() -> None:
    print("=== Player Score Analytics ===")
    analytics_argv(sys.argv)


if __name__ == "__main__":
    main()
