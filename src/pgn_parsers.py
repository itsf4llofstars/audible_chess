"""pgn_parsers.py"""

pattern = {
    "start": "1. ",
}


def read_file(filename: str) -> None:
    try:
        with open(filename) as read:
            file_lines = read.readlines()
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    else:
        index = 0
        for line in file_lines:
            if not line.startswith(pattern["start"]):
                file_lines.pop(index)
                index -= 1
            index += 1
        if file_lines:
            return file_lines
        else:
            raise Exception("File Parser Fail")


pgn_file_lines = read_file("/media/bumper/EDD2-E40F/raspi32/lichess_short.pgn")
[print(line) for line in pgn_file_lines]
