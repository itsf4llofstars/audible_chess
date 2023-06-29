"""fast_pgn_parsers.py file"""
import random
import re


def parse_pgn_file(
    filename,
    min_move: str = "20.",
    max_move: str = "40.",
    white: bool = True,
    mate: bool = False,
):
    games = []
    try:
        with open(filename, encoding="utf-8") as read:
            for line in read:
                line = line.strip()
                if (
                    not line.startswith("1. ")
                    or f" {max_move} " in line
                    or f" {min_move} " not in line
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

                if white and mate and "#" in line and line.endswith(" 1-0"):
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

    if games:
        return games
    return None


def get_study_game(games, min_move: str = "20", max_move: str = "40"):
    legal = re.compile(r"1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s[a-hBKNQR]")
    max_move = re.compile(r"\s" + max_move + r"\.\s")
    min_move = re.compile(r"\s" + min_move + r"\.\s")
    kibitz = re.compile(r"(\(|{|\[|<|>|\]|}|\))")

    annotates = ("!", "?", "+")

    while True:
        random_game = random.choice(games)

        if (
            not re.search(legal, random_game)
            or re.search(max_move, random_game)
            or not re.search(min_move, random_game)
            or re.search(kibitz, random_game)
        ):
            continue

        for annotate in annotates:
            random_game = random_game.replace(annotate, "")

        return random_game


def main():
    pgn_file = os.path.expanduser(os.path.join("~", "chess", "lichess_201407.pgn"))

    chess_games = parse_pgn_file(pgn_file)
    study_game = get_study_game(chess_games)
    print(study_game)


if __name__ == "__main__":
    import os

    main()
