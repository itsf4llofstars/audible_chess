"""fast_pgn_parsers.py file"""
import random


def parse_pgn_file(
    filename,
    min_move: str = "20.",
    max_move: str = "40.",
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
                    or f" {max_move} " in line
                    or f" {min_move} " in line
                    or "(" in line
                    or ")" in line
                    or "{" in line
                    or "}" in line
                    or "[" in line
                    or "]" in line
                    or "<" in line
                    or ">" in line
                ):
                    continue
                elif white and mate and "#" in line and line.endswith(" 1-0"):
                    games.append(line)
                elif white and not mate and "#" not in line and line.endswith(" 1-0"):
                    games.append(line)
                elif not white and mate and "#" in line and line.endswith(" 0-1"):
                    games.append(line)
                elif (
                    not white and not mate and "#" not in line and line.endswith(" 0-1")
                ):
                    games.append(line)

    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    finally:
        if games:
            return games


def get_study_game(games):
    pass


def main():
    pgn_file = os.path.expanduser(os.path.join("~", "chess", "lichess_201407.pgn"))

    chess_games = parse_pgn_file(pgn_file)
    study_game = get_study_game(chess_games)


if __name__ == "__main__":
    import os

    main()
