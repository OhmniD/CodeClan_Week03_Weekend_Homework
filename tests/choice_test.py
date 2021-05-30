import unittest
from models.choice import Choice

class TestChoice(unittest.TestCase):
    def setUp(self):
        self.rock = Choice('rock', 'scissors')
        self.paper = Choice('paper', 'rock')
        self.scissors = Choice('scissors', 'paper')

    def test_choice_has_name(self):
        expected = "rock"
        actual = self.rock.name
        self.assertEqual(expected, actual)

    def test_choice_has_object_it_beats(self):
        expected = "paper"
        actual = self.scissors.beats
        self.assertEqual(expected, actual)