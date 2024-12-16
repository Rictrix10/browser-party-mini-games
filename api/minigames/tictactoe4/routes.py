from flask import Blueprint, request, jsonify
from .logic import init_game, make_move, reset_game

# Criação do Blueprint
tictactoe4_bp = Blueprint('tictactoe4', __name__)

# Estado do jogo compartilhado
game_state = init_game()

@tictactoe4_bp.route('/play', methods=['POST'])
def play():
    data = request.json
    username = data.get("username")
    col = data.get("column")
    row = data.get("row")

    # Validações e lógica de jogada
    try:
        updated_board, winner = make_move(game_state, username, row, col)
        return jsonify({
            "board": updated_board,
            "winner": winner
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tictactoe4_bp.route('/reset', methods=['POST'])
def reset():
    reset_game(game_state)
    return jsonify({"message": "Game reset successfully", "board": game_state['board']})
