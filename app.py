from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame
from wordlist import WordList

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    game_info = {"gameId": game_id, "board": game.board}
    return jsonify(game_info)

@app.post("/api/score-word")
def score_word():
    """ checks if word is legal, 
    takes game id and the word in json, 
    returns json response (use jsonify)"""

    gameId_response = request.json['gameId']
    word_response = request.json['word']
    game = BoggleGame()
    english_words = WordList("dictionary.txt")

    if type(word_response) != 'string':
        return {'result': 'not-word'}
    if game.check_word_on_board(word_response) == False:
        return {'result': 'not-on-board'}
    if word_response in english_words:
        return {'restult': 'ok'}

    breakpoint()


