from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game
from random import choice

title="Rock, Paper, Scissors"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title=title)

@app.route('/<player1_choice>/<player2_choice>')
def index(player1_choice, player2_choice):
    player1 = Player("Player 1", player1_choice)
    player2 = Player("Player 2", player2_choice)
    game = Game()
    game_result = game.game_logic(player1, player2)
    return render_template('index.html', title=title, game_result=game_result, player1=player1, player2=player2)

@app.route('/play')
def play_computer_show():
    return render_template('play.html', title=title, game_result="unplayed")

@app.route('/play', methods=['POST'])
def play_computer_post():
    player_name = request.form['name']
    player_choice = request.form['choice']
    player1 = Player(player_name, player_choice)
    computer_choice = choice(['rock', 'paper', 'scissors'])
    player2 = Player("Computer", computer_choice)
    game = Game()
    game_result = game.game_logic(player1, player2)
    return render_template('play.html', title=title, game_result=game_result, player1=player1, player2=player2)