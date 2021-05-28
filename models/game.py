## when making computer function, re-use game rules function
from models.choice import Choice

# Can't escape the feeling that this is a bit of a mess and there's a better way to do it
# Was trying to use a choice class so could be expanded if required (e.g. with lizard, spock)
# By converting choice.beats to a list, as in the preferred task lab

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
        
