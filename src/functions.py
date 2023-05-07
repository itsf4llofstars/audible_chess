"""functions.py"""
import re


def regex_pgn_file(filename: str) -> object:
    """Read a chess pgn file and return
    those lines beginning with "^(1.\s)" and end with
    "(\s[1-0|0-1])$" as a list of str's

    Requires import re
    """
    game_begin = re.compile(r"^(1\.\s1\s)")
    game_end = re.compile(r"(\s[1-0|0-1])$")
    chess_games = list()

    try:
        with open(filename) as read:
            for line in read:
                if re.seaerch(game_begin, line) and re.search(game_end, line.rtrip()):
                    chess_games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        # Log this
        print(f"{fnfe}")
    finally:
        if chess_games:
            return chess_games
        return


def main():
    ...


if __name__ == "__main__":
    main()
