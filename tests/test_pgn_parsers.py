"""test_pgn_parsers.py"""
import os
import unittest

from src.pgn_parsers import min_max_move
from src.pgn_parsers import read_file

test_moves = [
    "1. xx xx 19. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 40. xx xx",
    "1. xx xx 40. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 33. xx xx",
]


class TestGamesList(unittest.TestCase):
    """Unittests to test the pgn_parser.py file
    functions
    """

    def test_read_file(self):
        unittest_pgn = os.path.expanduser(
            os.path.join("~", "python", "audible_chess", "docs", "test_read_file.pgn")
        )
        test_chess_games = read_file(unittest_pgn)
        self.assertEqual(test_chess_games, ["1. xx xx 2. xx xx", "1. xx xx 2. xx xx"])

    def test_min_max_move(self):
        test_chess_games = min_max_move(test_moves)
        self.assertEqual(test_chess_games, ["1. xx xx 20. xx xx 39. xx xx", "1. xx xx 20. xx xx 33. xx xx"])


if __name__ == "__main__":
    unittest.main()
