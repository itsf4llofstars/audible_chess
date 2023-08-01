"""parser_class.py"""
import os
import re


class Parser:
    def __init__(self, filename: str):
        self.filename = filename
        self.raw_games = []
        self.patterns = {
            "start": "1. ",
            "star_re": re.compile(r"1\.\s"),
            "legal_re": re.compile(r"^1\.\s[a-hN][3-4acfg]3?\s[a-hN][5-6acfg]6?\s2\.\s"),
            "to_long": " 40. ",
            "to_short": " 20. ",  # should be changed for production release
            "paren_o": "(",
            "paren_c": ")",
            "brace_o": "{",
            "brace_c": "}",
            "bracket_o": "[",
            "bracket_c": "]",
            "tag_o": "<",
            "tag_c": ">",
            "white": re.compile(" 1-0"),
            "black": re.compile(" 0-1"),
            "draw": re.compile(" 1/2-1/2"),
            "mate": re.compile("#"),
        }
        self.annotations = ["!", "?", "+"]

    def print_games(self):
        [print(game) for game in self.raw_games]

    def read_file(self):
        try:
            with open(self.filename, encoding="utf-8") as read:
                [self.raw_games.append(line.rstrip()) for line in read
                 if not line.startswith(self.patterns["start"])]
        except FileNotFoundError as fnfe:
            raise FileNotFoundError("File not found") from fnfe

    def clean_all(self):
        index = 0
        while index < len(self.raw_games):
            if (
                self.patterns["paren_o"] in self.raw_games[index]
                or self.patterns["paren_c"] in self.raw_games[index]
            ):
                self.raw_games.pop(index)
            elif (
                self.patterns["brace_o"] in self.raw_games[index]
                or self.patterns["brace_c"] in self.raw_games[index]
            ):
                self.raw_games.pop(index)
            elif (
                self.patterns["bracket_o"] in self.raw_games[index]
                or self.patterns["bracket_c"] in self.raw_games[index]
            ):
                self.raw_games.pop(index)
            elif (
                self.patterns["tag_o"] in self.raw_games[index]
                or self.patterns["tag_c"] in self.raw_games[index]
            ):
                self.raw_games.pop(index)
            elif (
                self.patterns["to_long"] in self.raw_games[index]
                or self.patterns["to_short"] not in self.raw_games[index]
            ):
                self.raw_games.pop(index)
            else:
                index += 1


def main():
    pgn_name = os.path.expanduser(os.path.join("~", "chess", "chess.pgn"))
    parser = Parser(pgn_name)
    parser.clean_all()
    parser.print_games()


if __name__ == "__main__":
    main()
