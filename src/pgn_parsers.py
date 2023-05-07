"""pgn_parsers.py"""
import re

regex = {"min_move": r"", "max_move": r""}


def get_game_length(move_min: str, move_max: str, games) -> object:
    length_games = []
    regex["min_move"] = r"\s" + move_min + r"\.\s"
    regex["max_move"] = r"\s" + move_max + r"\.\s"

    for game in games:
        if re.search(regex["min_move"], game) and not re.search(
            regex["max_move"], game
        ):
            length_games.append(game)

    return length_games


def main():
    game_list = [
        "1. xx xx 2. xx xx 10. NO xx 11. xx xx 40. xx xx 41. xx xx",
        "1. xx xx 2. xx xx 10. YE xx 11. xx xx 38. xx xx 39. xx xx",
        "1. xx xx 2. xx xx 10. NO xx 11. xx xx 40. xx xx 41. xx xx",
        "1. xx xx 2. xx xx 10. YE xx 11. xx xx 38. xx xx 39. xx xx",
    ]

    chess_games = get_game_length("10", "40", game_list)
    [print(game) for game in chess_games]


if __name__ == "__main__":
    main()
