"""The functions.py Python file."""
import os
import re
import sys
from pgn_parsers import regex


def regex_pgn_file(filename: str) -> object:
    r"""Read a chess pgn file. ("r" is to prevent flake8 errors)

    Return those lines beginning with "^(1\.\s)"
    and end with "(\s[1-0|0-1])$" as a list of str's

    Args:
        filename (str): Path and name of the pgn file

    Returns:
        List(str): Only strings of chess games
    """
    game_begin = re.compile(r"^(1\.\s)")
    game_end = re.compile(r"(\s[0-1]|[0-1])$")
    chess_games = []

    try:
        with open(filename, encoding="utf-8") as read:
            for line in read:
                if re.search(game_begin, line) and re.search(game_end, line.rstrip()):
                    chess_games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")

    return chess_games


def fast_pgn_file(filename: str):
    """Read a chess pgn file

    Return those lines that begin with "1. " and end with
    either " 1-0", "0-1", " 1/2-1/2", using no regex for
    fasters parsing of large files.

    Args:
        filename (str): Path and name of the pgn file

    Returns:
        List(str): Only strings of chess games
    """
    start = "1. "
    white = " 1-0"
    black = " 0-1"
    draw = " 1/2-1/2"
    pgn_games = []
    try:
        with open(filename) as read:
            for line in read:
                line = line.strip()
                if line.startswith(start) and (
                    line.endswith(white) or line.endswith(black) or line.endswith(draw)
                ):
                    pgn_games.append(line)
    except FileNotFoundError:
        print("File not found: fast_pgn_file()")
        sys.exit()
    else:
        if pgn_games:
            return pgn_games


def set_max_move(max_move):
    regex["max_move_re"] = r"\s" + str(max_move) + r"\.\s"
    regex["max_move"] = f" {max_move}. "


def get_ending() -> str:
    return str(input("\tCHOICE: "))


def get_strip_mate() -> str:
    return str(input("\tWould your like to strip that last mate move? [y/n]: "))


def get_max_move() -> int:
    move = None
    while True:
        try:
            move = int(input("\tEnter your maximum number of moves: "))
        except Exception:
            ...
        finally:
            if isinstance(move, int):
                if 20 < move < 100:
                    return move
                print("\n\tEnter a number 21 - 99\n")
                continue
            print("\n\tPlease enter only and integer\n")
            continue


def main():
    pgn_name = os.path.expanduser(
        os.path.join("~", "python", "audible_chess", "docs", "for_tests.pgn"),
    )

    # games = regex_pgn_file(pgn_name)
    games = fast_pgn_file(pgn_name)
    for game in games:
        print(game)


if __name__ == "__main__":
    main()
