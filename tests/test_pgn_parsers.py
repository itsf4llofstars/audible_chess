"""test_pgn_parsers.py"""
import os
import unittest

from src.pgn_parsers import read_file


class TestGamesList(unittest.TestCase):
    """Unittests to test the pgn_parser.py file
    functions
    """

    def test_read_file(self):
        unittest_pgn = os.path.expanduser(
            os.path.join("~", "pythone", "audible_chess", "docs", "uinttest.pgn")
        )
        test_chess_games = read_file(unittest_pgn)
        self.assertEqual(
            test_chess_games, ["1. xx xx 2. xx xx", "1. xx xx 2. xx xx"]]
        )


if __name__ == "__main__":
    unittest.main()
