import unittest
from models.player import Player
from models.choice import Choice
from models.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):

        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "scissors")

        self.game = Game(self.player1, self.player2)

    def test_player_1_wins(self):
        expected = "Player 1"
        actual = self.game.game_logic()
        self.assertEqual(expected, actual)

    def test_player_2_wins(self):
        self.player1.choice = "paper"
        expected = "Player 2"
        actual = self.game.game_logic()
        self.assertEqual(expected, actual)

    def test_players_choose_same_thing(self):
        self.player2.choice = "rock"
        expected = None
        actual = self.game.game_logic()
        self.assertEqual(expected, actual)

    def test_mixed_case_input_for_game_choice(self):
        self.player1.choice = "RoCk"
        expected = "Player 1"
        actual = actual = self.game.game_logic()
        self.assertEqual(expected, actual)