"""fast_pgn_parsers.py file"""


def plarse_pgn_file(
    filename,
    min_move: str = " 20. ",
    max_move: str = " 40. ",
    white: bool = True,
    mate: bool = False,
):
    games = []
    try:
        with open(filename) as read:
            for line in read:
                line = line.strip()
                if (
                    not line.startswith("1. ")
                    or " 40. " in line
                    or " 20. " not in line
                    or "(" in line
                    or "{" in line
                    or "[" in line
                    or "<" in line
                ):
                    continue
                else:
                    games.append(line)

    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    else:
        pass
    finally:
        pass


def main():
    pass


if __name__ == "__main__":
    main()
