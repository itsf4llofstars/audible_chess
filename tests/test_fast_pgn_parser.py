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
            os.path.join("~", "python", "audible_chess", "docs", "fast_parse_test.pgn")
        )
        test_chess_games = parse_pgn_file(unittest_pgn)
        self.assertEqual(
            test_chess_games,
            [
                "1. x xx 2. xx xx 20. xx xx 4. xx xx 5. xx 1-0",
                "1. xx xx 2. xx xx 20. xx xx 4. xx xx 5. xx 1-0",
            ],
        )


if __name__ == "__main__":
    unittest.main()
