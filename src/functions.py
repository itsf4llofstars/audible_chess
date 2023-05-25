"""The functions.py Python file."""
import os
import re
import sys

from pgn_parsers import pattern


def get_users_choice() -> int:
    """Error checking required"""
    while True:
        choice = int(input("\tChoice (1 - 6): "))
        if 1 <= choice < 6:
            return choice
        elif choice == 6:
            sys.exit()
        else:
            print("\n\tEnter a number between 1 and 6 or 0 to exit.\n")


def get_moves() -> int:
    """Error checking required"""
    while True:
        moves = int(input("\tEnter your max moves (21 - 99) 0 to quit: "))
        if 20 < moves < 100:
            moves += 1
            return moves
        elif moves == 0:
            sys.exit()
        else:
            print("\n\tPlease enter a number between 21 and 99 or 0 to quit.\n")


def strip_mate_query() -> bool:
    """Error check required"""
    strip_mate = str(
        input("\n\n\tDo you wish to strip the last checkmating move? (y/n): ")
    )
    strip_mate = strip_mate.strip().lower()

    if strip_mate[0] == "y" or strip_mate[0] == "n":
        if strip_mate[0] == "y":
            return True
        elif strip_mate[0] == "n":
            return False
    elif strip_mate[0] != "y" or strip_mate[0] != "n":
        raise ValueError("A [y]es or [n]o was not entered.")


def move_seconds() -> int:
    """Error check needed"""
    seconds = int(input("\n\n\tPlease enter the number of seconds between each move: "))
    assert isinstance(seconds, int)
    assert seconds > 4
    return seconds


def regex_pgn_file(filename: str):
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
    pattern["max_move_re"] = r"\s" + str(max_move) + r"\.\s"
    pattern["max_move"] = f" {max_move}. "


def main():
    games = regex_pgn_file("/home/bumper/python/audible_chess/docs/test_read_file.pgn")
    print(games)


if __name__ == "__main__":
    os.system("clear")
    main()
