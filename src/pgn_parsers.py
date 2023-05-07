"""pgn_parsers.py"""
import re

regex = {"min_move": r"", "max_move": r""}


def get_game_length(move_min: str, move_max: str, games) -> object:
    length_games = []
    regex["min_move"] = r"\s" + move_min + r"\.\s"
    regex["max_move"] = r"\s" + move_max + r"\.\s"

    for game in games:
        if re.search(regex["min_move"], game) and not re.search(["regex"], game):
            length_games.append(game)

    return length_games


def main():
    ...


if __name__ == "__main__":
    main()
