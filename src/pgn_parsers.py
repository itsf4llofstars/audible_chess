"""pgn_parsers.py"""
import os

pattern = {
    "start": "1. ",
    "min_move": " 20. ",
    "max_move": " 40. ",  # NOTE: Must be removed for final release. Must be 40 for tests
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


def main():
    pgn_file = os.path.expanduser(os.path.join("~", "chess", "bumper.pgn"))

    chess_games = read_file(pgn_file)
    chess_games = min_max_move(chess_games)
    print(len(chess_games))
    print(chess_games[10])
    # [print(game) for game in chess_games]


if __name__ == "__main__":
    main()
