from models.choice import Choice
from models.player import Player
from random import choice 

# Can't escape the feeling that this is a bit of a mess and there's a better way to do it
# Was trying to use a choice class so could be expanded if required (e.g. with lizard, spock)...
# ...by converting choice.beats to a list, as in the preferred task lab
# Possible addition - logic to check if the inputs are valid rather than going straight to player 2 winning

class Game:
    def __init__(self):
        self.rock = Choice('rock', 'scissors')
        self.paper = Choice('paper', 'rock')
        self.scissors = Choice('scissors', 'paper')
        self.choices = [self.rock, self.paper, self.scissors]
    
    def game_logic(self, player1, player2): 
        player1_beats = ""
        for choice in self.choices:
            if player1.choice.lower() == choice.name:
                player1_beats = choice.beats

        if player1.choice == player2.choice:
            return None
        elif player1_beats == player2.choice:
            return player1.name
        else:
            return player2.name
    

        
