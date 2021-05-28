from flask import render_template
from app import app
from models.player import Player
from models.game import Game

@app.route('/<player1_choice>/<player2_choice>')
def index(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    game = Game(player1, player2)
    game_result = game.game_logic()
    return render_template('index.html', title="Rock, Paper, Scissors", game_result=game_result)
