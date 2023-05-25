"""test_functions.py"""
import os
import unittest

from src.functions import regex_pgn_file


class TestFunctionsFile(unittest.TestCase):
    def test_regex_pgn_file(self):
        test_pgn = os.path.expanduser(
            os.path.join("~", "python", "audible_chess", "docs", "test_read_file.pgn")
        )
        test_games_list = regex_pgn_file(test_pgn)
        self.assertEqual(
            test_games_list, ["1. xx xx 2. xx xx 1-0", "1. xx xx 2. xx xx 0-1"]
        )


if __name__ == "__main__":
    unittest.main()
