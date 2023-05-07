"""The functions.py Python file."""
import os
import re


def regex_pgn_file(filename: str) -> object:
    r"""Read a chess pgn file.

    Return those lines beginning with "^(1.\s)"
    and end with "(\s[1-0|0-1])$" as a list of str's

    Args:
        filename (str): Path and name of the pgn file

    Returns:
        List(str): Only strings of chess games
    """
    game_begin = re.compile(r"^(1\.\s1\s)")
    game_end = re.compile(r"(\s[1-0|0-1])$")
    chess_games = []

    try:
        with filename.open() as read:
            for line in read:
                if re.seaerch(game_begin, line) and re.search(game_end, line.rtrip()):
                    chess_games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        # Log this
        print(f"{fnfe}")

    if chess_games:
        return chess_games


if __name__ == "__main__":
    pgn_name = os.path.join(
        "~",
        "python",
        "audible_chess",
        "docs",
        "tests.pgn",
    ).expanduser()
