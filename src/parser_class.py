"""parser_class.py"""
imoprt re


class Parser:
    def __init__(self, filename: str):
        self._filename = filename
        self.raw_games = []
        self.patterns = {
            "start": "1. ",
            "star_re": r"1\.\s",
            "legal_re": r"^1\.\s[a-hN][3-4acfg]3?\s[a-hN][5-6acfg]6?\s2\.\s",
        }

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        if not isinstance(filename, str):
            raise ValueError("Filename is not a string")
        self._filename = filename

    def read_file(self):
        try:
            with open(self.filename, encoding="utf-8") as read:
                for line in read:


def main():
    ...


if __name__ == "__main__":
    main()
