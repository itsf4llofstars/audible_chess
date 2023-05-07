"""test_functions.py"""
import unittest
from src.functions import regex_pgn_file


class TestFuncitions(unittest.TestCase):
    """Tests for the functions.py file"""

    def test_regex_pgn_file(self):
        """Test to show function returns proper beginning
        and end of the chess games. This uses the unittest.pgn
        file
        """
        test_games = regex_pgn_file("~/python/audible_chess_docs/unittest.pgn")
        self.assertEqual(["1. xx xx 2. xx xx 1-0", "1. xx xx 2. xx 0-1"])


if __name__ == "__main__":
    unittest.main()
