"""parser_class.py"""


class Parser:
    def __init__(self, filename: str):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        if not isinstance(filename, str):
            raise ValueError("Filename is not a string")
        self._filename = filename


def main():
    ...


if __name__ == "__main__":
    main()
