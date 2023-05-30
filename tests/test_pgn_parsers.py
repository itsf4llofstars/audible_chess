"""test_pgn_parsers.py"""
import os
import unittest

from src.pgn_parsers import min_max_move
from src.pgn_parsers import read_file
from src.pgn_parsers import no_kibitz
from src.pgn_parsers import scrub_annotations
from src.pgn_parsers import get_white_mates
from src.pgn_parsers import get_white_wins
from src.pgn_parsers import get_black_mates
from src.pgn_parsers import get_black_wins

test_moves = [
    "1. xx xx 19. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 40. xx xx",
    "1. xx xx 40. xx xx 39. xx xx",
    "1. xx xx 20. xx xx 33. xx xx",
]

test_kibitz = [
    "1. xx xx 2. ( xx xx ) 3. xx xx",
    "1. xx xx 2. ( xx xx 3. xx xx",
    "1. xx xx 2. ) xx xx 3. xx xx",
    "1. xx xx 2. xx xx 3. xx xx",
    "1. xx xx 2. { xx xx } 3. xx xx",
    "1. xx xx 2. xx xx } 3. xx xx",
    "1. xx xx 2. { xx xx 3. xx xx",
    "1. xx xx 2. [ xx xx ] 3. xx xx",
    "1. xx xx 2. xx xx ] 3. xx xx",
    "1. xx xx 2. [ xx xx 3. xx xx",
    "1. xx xx 2. < xx xx > 3. xx xx",
    "1. xx xx 2. xx xx 3. xx xx",
    "1. xx xx 2. xx xx > 3. xx xx",
    "1. xx xx 2. < xx xx 3. xx xx",
]

test_annotations = [
    "1. xx xx! 2. xx!! xx? 3. xx?? xx",
    "1. xx xx?! 2. xx!? xx+ 3. xx xx",
    "1. xx xx 2. xx xx 3. xx xx",
]

winners_list = [
    "1. xx xx 2. xx xx 3. xx xx",
    "1. xx xx 2. xx xx 3. xx xx# 1-0",
    "1. xx xx 2. xx xx 3. xx xx 1/2-1/2",
    "1. xx xx 2. xx xx 3. xx xx 0-1",
    "1. xx xx 2. xx xx 3. xx xx",
    "1. xx xx 2. xx xx 3. xx xx 1-0",
    "1. xx xx 2. xx xx 3. xx xx# 0-1",
    "1. xx xx 2. xx xx 3. xx xx 1/2-1/2",
    "1. xx xx 2. xx xx 3. xx xx *",
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
        self.assertEqual(
            test_chess_games, ["1. xx xx 2. xx xx 1-0", "1. xx xx 2. xx xx 0-1"]
        )

    def test_min_max_move(self):
        test_chess_games = min_max_move(test_moves)
        self.assertEqual(
            test_chess_games,
            ["1. xx xx 20. xx xx 39. xx xx", "1. xx xx 20. xx xx 33. xx xx"],
        )

    def test_no_kibitz(self):
        test_chess_games = no_kibitz(test_kibitz)
        self.assertEqual(
            test_chess_games,
            ["1. xx xx 2. xx xx 3. xx xx", "1. xx xx 2. xx xx 3. xx xx"],
        )

    def test_scrub_annotations(self):
        test_chess_games = scrub_annotations(test_annotations)
        self.assertEqual(
            test_annotations,
            [
                "1. xx xx 2. xx xx 3. xx xx",
                "1. xx xx 2. xx xx 3. xx xx",
                "1. xx xx 2. xx xx 3. xx xx",
            ],
        )

    def test_get_white_mates(self):
        test_white_mates = get_white_mates(winners_list)
        self.assertEqual(test_white_mates, ["1. xx xx 2. xx xx 3. xx xx# 1-0"])

    def test_get_white_wins(self):
        test_white_wins = get_white_wins(winners_list)
        self.assertEqual(test_white_wins, ["1. xx xx 2. xx xx 3. xx xx 1-0"])

    def test_get_black_mates(self):
        test_black_mates = get_black_mates(winners_list)
        self.assertEqual(test_black_mates, ["1. xx xx 2. xx xx 3. xx xx# 0-1"])


if __name__ == "__main__":
    unittest.main()
