from models.choice import Choice
from models.player import Player
from random import choice 

# Can't escape the feeling that this is a bit of a mess and there's a better way to do it
# Was trying to use a choice class so could be expanded if required (e.g. with lizard, spock)...
# ...by converting choice.beats to a list, as in the preferred task lab
# Possible addition - logic to check if the inputs are valid rather than going straight to player 2 winning

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def game_logic(self):
        self.rock = Choice('rock', 'scissors')
        self.paper = Choice('paper', 'rock')
        self.scissors = Choice('scissors', 'paper')
        choices = [self.rock, self.paper, self.scissors]
        
        player1_beats = ""
        for choice in choices:
            if self.player1.choice.lower() == choice.name:
                player1_beats = choice.beats

        if self.player1.choice == self.player2.choice:
            return None
        elif player1_beats == self.player2.choice:
            return self.player1.name
        else:
            return self.player2.name
    
    # def play_computer(self, player1):
    #     self.player1 = player1
    #     computer_choice = random.choice(['rock', 'paper', 'scissors'])
    #     self.player2 = Player("Computer", computer_choice)
    #     self.game_logic()

    

        
