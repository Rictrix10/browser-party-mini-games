from flask import Flask
from minigames.tictactoe4.routes import tictactoe4_bp
from minigames.random_pick.routes import random_pick_bp

app = Flask(__name__)

# Registra os blueprints dos minigames
app.register_blueprint(tictactoe4_bp, url_prefix='/tictactoe4')

app.register_blueprint(random_pick_bp, url_prefix='/random_pick')

@app.route('/')
def index():
    return {
        "message": "Welcome to the Browser Party Minigames!",
        "games": [
            {"name": "TicTacToe4", "endpoint": "/tictactoe4"}
        ]
    }

if __name__ == '__main__':
    app.run(debug=True)
