import unittest
from unittest.mock import patch
from player import Player

# python3 -m unittest test_player.py

class TestPlayer(unittest.TestCase):
    @patch("builtins.input", side_effect=["John","x"])
    def test_choose_name_invalid_input(self, mock_input):
        player = Player()
        player.choose_name()
        player.choose_symbol()
        self.assertEqual(player.name, "John")
        self.assertEqual(player.symbol, "X")
    
    @patch("builtins.input", side_effect=["x"])
    def test_choose_symbol_invalid_input(self, mock_input):
        player = Player()
        player.choose_symbol()
        self.assertEqual(player.symbol, "X")


if __name__ == "__main__":
    unittest.main()
