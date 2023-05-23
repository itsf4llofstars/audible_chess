"""pgn_parsers.py"""

pattern = {
    "start": "1. ",
    "min_move": " 20. ",
    "max_move": " 30. ",  # NOTE: Must be removed for final release
}


def read_file(filename: str) -> None:
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


def main():
    # chess_games = read_file("/media/bumper/EDD2-E40F/raspi32/lichess_short.pgn")
    chess_games = read_file("/home/bumper/python/audible_chess/docs/test_read_file.pgn")

    [print(line) for line in pgn_file_lines]


if __name__ == "__main__":
    main()
