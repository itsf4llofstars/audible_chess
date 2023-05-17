"""The functions.py Python file."""
import os
import re


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


if __name__ == "__main__":
    pgn_name = os.path.expanduser(
        os.path.join("~", "python", "audible_chess", "docs", "for_tests.pgn"),
    )

    games = regex_pgn_file(pgn_name)
    for game in games:
        print(game)
