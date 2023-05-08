"""test_pgn_parsers.py"""
import unittest

from src.pgn_parsers import get_game_length

game_lengths = [
    "1. xx 10. xx 40. xx",
    "1. xx 9. xx 39. xx",
    "1. xx 10. xx 39. xx",
    "1. xx 2. xx 10. x 25.",
    "1. xx 9. xx 40. xx",
]


class TestGamesList(unittest.TestCase):
    """Unittests to test the pgn_parser.py file
    functions
    """

    def test_get_game_length(self):
        """Test if returned games has the min_move and not the
        max_move in them
        """
        test_chess_games = get_game_length("10", "40", game_lengths)
        self.assertEqual(test_chess_games, ["1. xx 10. xx 39. xx", "1. xx 2. xx 10. x 25."])


if __name__ == "__main__":
    unittest.main()
