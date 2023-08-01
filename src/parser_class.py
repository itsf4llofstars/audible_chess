"""parser_class.py"""
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
            "white": " 1-0",
            "black": " 0-1",
            "draw": " 1/2-1/2",
            "mate": "#",
        }

    def read_file(self):
        try:
            with open(self.filename, encoding="utf-8") as read:
                [self.raw_games.append(line.rstrip()) for line in read
                 if not line.startswith(self.patterns["start"])]
        except FileNotFoundError as fnfe:
            raise FileNotFoundError("File not found") from fnfe


def main():
    ...


if __name__ == "__main__":
    main()
