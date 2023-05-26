"""pgn_parsers.py"""
import os

pattern = {
    "start": "1. ",
    "min_move": " 20. ",
    "max_move": " 40. ",  # NOTE: Must be removed for final release. Must be 40 for tests
    "paren_o": "(",
    "paren_c": ")",
    "brace_o": "{",
    "brace_c": "}",
    "bracket_o": "[",
    "bracket_c": "]",
    "tag_o": "<",
    "tag_c": ">",
    "white_wins": " 1-0",
    "black_wins": " 0-1",
    "hash": "#",
}


def read_file(filename: str):
    games = []
    try:
        with open(filename) as read:
            for line in read:
                if line.startswith(pattern["start"]):
                    games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    finally:
        if games:
            return games


def min_max_move(games):
    index = 0
    while index < len(games):
        if (
            not pattern["min_move"] in games[index]
            or pattern["max_move"] in games[index]
        ):
            games.pop(index)
            index -= 1

        index += 1
    return games


def no_kibitz(games):
    index = 0
    while index < len(games):
        if (
            pattern["paren_o"] in games[index]
            or pattern["paren_c"] in games[index]
            or pattern["brace_o"] in games[index]
            or pattern["brace_c"] in games[index]
            or pattern["bracket_o"] in games[index]
            or pattern["bracket_c"] in games[index]
            or pattern["tag_o"] in games[index]
            or pattern["tag_c"] in games[index]
        ):
            games.pop(index)
            index -= 1

        index += 1
    return games


def scrub_annotations(games):
    """DOC"""
    annotations = ["!", "?", "+"]
    index = 0
    while index < len(games):
        for annotate in annotations:
            games[index] = games[index].replace(annotate, "")
        index += 1
    return games


def white_mates(games):
    index = 0
    while index < len(games):
        if not games[index].endswith(pattern["white_wins"]) and not pattern["hash"] in games[index]:
            games.pop(index)
            index -=1

        index += 1
    return games


def white_wins(games):
    index = 0
    while index < len(games):
        index += 1
    return games


def black_mates(games):
    index = 0
    while index < len(games):
        index += 1
    return games


def black_wins(games):
    index = 0
    while index < len(games):
        index += 1
    return games


def main():
    pgn_file = os.path.expanduser(os.path.join("~", "chess", "chess.pgn"))

    chess_games = read_file(pgn_file)
    chess_games = min_max_move(chess_games)
    chess_games = no_kibitz(chess_games)
    chess_games = scrub_annotations(chess_games)

    if white:
        if mate:
            get_white_mates(chess_games)
        else:
            get_white_wins(chess_games)
    elif not white:
        if mate:
            get_black_mates(chess_games)
        else:
            get_black_wins(chess_games)

    [print(game) for game in chess_games]


if __name__ == "__main__":
    main()
