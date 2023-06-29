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
    """Needs Doc. Has test"""
    games = []
    try:
        with open(filename, encoding="utf-8") as read:
            for line in read:
                if line.startswith(pattern["start"]):
                    games.append(line.rstrip())
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    return games


def min_max_move(games):
    """Needs Doc. Has Test"""
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
    """Needs Doc. Has test"""
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
    """Needs Doc. Has test"""
    annotations = ["!", "?", "+"]
    index = 0
    while index < len(games):
        for annotate in annotations:
            games[index] = games[index].replace(annotate, "")
        index += 1
    return games


def get_white_mates(games):
    """docstring"""
    index = 0
    while index < len(games):
        if not pattern["hash"] in games[index]:
            games.pop(index)
            index -= 1
        elif games[index].endswith(pattern["black_wins"]):
            games.pop(index)
            index -= 1

        index += 1
    return games


def get_white_wins(games):
    """docstring"""
    index = 0
    while index < len(games):
        if pattern["hash"] in games[index]:
            games.pop(index)
            index -= 1
        elif games[index].endswith(pattern["black_wins"]):
            games.pop(index)
            index -= 1
        elif not games[index].endswith(pattern["white_wins"]):
            games.pop(index)
            index -= 1
        index += 1

    return games


def get_black_mates(games):
    """docstring"""
    index = 0
    while index < len(games):
        if not pattern["hash"] in games[index]:
            games.pop(index)
            index -= 1
        elif games[index].endswith(pattern["white_wins"]):
            games.pop(index)
            index -= 1

        index += 1
    return games


def get_black_wins(games):
    """docstring"""
    index = 0
    while index < len(games):
        if pattern["hash"] in games[index]:
            games.pop(index)
            index -= 1
        elif games[index].endswith(pattern["white_wins"]):
            games.pop(index)
            index -= 1
        elif not games[index].endswith(pattern["black_wins"]):
            games.pop(index)
            index -= 1
        index += 1
    return games


if __name__ == "__main__":
    var_games = [
        "1. xx xx 2. xx xx 3. xx xx",
        "1. xx xx 2. xx xx 3. xx xx# 0-1",
        "1. xx xx 2. xx xx 3. xx xx# 0-1",
        "1. xx xx 2. xx xx 3. xx xx 1-0",
        "1. xx xx 2. xx xx 3. xx xx# 1-0",
        "1. xx xx 2. xx xx 3. xx xx 0-1",
        "1. xx xx 2. xx xx 3. xx xx 1/2-1/2",
        "1. xx xx 2. xx xx 3. xx xx 1-0",
        "1. xx xx 2. xx xx 3. xx xx",
        "1. xx xx 2. xx xx 3. xx xx# 0-1",
        "1. xx xx 2. xx xx 3. xx xx# 1-0",
        "1. xx xx 2. xx xx 3. xx xx 1-0",
        "1. xx xx 2. xx xx 3. xx xx 1/2-1/2",
    ]

    INDEX = 0
    while INDEX < len(var_games):
        if pattern["hash"] in var_games[INDEX]:
            var_games.pop(INDEX)
            INDEX -= 1
        elif var_games[INDEX].endswith(pattern["black_wins"]):
            var_games.pop(INDEX)
            INDEX -= 1
        elif not var_games[INDEX].endswith(pattern["white_wins"]):
            var_games.pop(INDEX)
            INDEX -= 1
        INDEX += 1
        os.system("clear")

        for game in var_games:
            print(game)
