"""test_fast_parser.py"""
import os
import unittest

from src.fast_pgn_parser import parse_pgn_file


class TestFastParsers(unittest.TestCase):
    """Unittest  to test the fast_pgn_parser.py
    file
    """

    def test_parse_pgn_file(self):
        unittest_pgn = os.path.expanduser(
            os.path.join("~", "python", "audible_chess", "docs", "test_read_file.pgn")
        )
        test_chess_games = parse_pgn_file(unittest_pgn)
        self.assertEqual(test_chess_games, ["1. "], ["1. "])


if __name__ == "__main__":
    unittest.main()
