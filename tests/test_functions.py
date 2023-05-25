"""test_functions.py"""
import os
import unittest
from src.functions import regex_pgn_file


class TestFunctions(unittest.TestCase):
    """Tests for the functions.py file"""

    def test_regex_pgn_file(self):
        """Test to show function returns proper beginning
        and end of the chess games. This uses the unittest.pgn
        file
        """
        test_pgn = os.path.expanduser(
            os.path.join("~", "python", "audible_chess", "docs", "test_read_file.pgn")
        )
        test_games = regex_pgn_file(test_pgn)
        self.assertEqual(test_games, ["1. e4 e5 2. Nf3 Nc6 1-0", "1. e4 e5 2. Nf3 0-1"])


if __name__ == "__main__":
    unittest.main()
