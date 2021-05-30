from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game
from random import choice

#TODO - refactor so play against computer runs as method rather than in controller
# Fix bug where "wins!" appears on play page before any result is shown
# Add what each user picked to page

title="Rock, Paper, Scissors"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title=title)

@app.route('/<player1_choice>/<player2_choice>')
def index(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    game = Game(player1, player2)
    game_result = game.game_logic()
    return render_template('index.html', title=title, game_result=game_result)

@app.route('/play')
def play_computer_show():
    return render_template('play.html', title=title)

@app.route('/play', methods=['POST'])
def play_computer_post():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player1 = Player(player_name, player_choice)
    computer_choice = choice(['rock', 'paper', 'scissors'])
    player2 = Player("Computer", computer_choice)
    game = Game(player1, player2)
    game_result = game.game_logic()
    return render_template('play.html', title=title, game_result=game_result)