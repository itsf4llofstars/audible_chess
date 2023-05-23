"""pgn_parsers.py"""

pattern = {
    "start": "1. ",
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


# pgn_file_lines = read_file("/media/bumper/EDD2-E40F/raspi32/lichess_short.pgn")
pgn_file_lines = read_file("/home/bumper/python/audible_chess/docs/unittest.pgn")
[print(line) for line in pgn_file_lines]
