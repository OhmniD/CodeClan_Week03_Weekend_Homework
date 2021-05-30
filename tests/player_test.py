import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Dave", "Scissors")
    
    def test_player_has_name(self):
        expected = "Dave"
        actual = self.player1.name
        self.assertEqual(expected, actual)

    def test_player_has_game_choice(self):
        expected = "scissors"
        actual = self.player1.choice
        self.assertEqual(expected, actual)