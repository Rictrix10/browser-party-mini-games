from flask import Blueprint, request, jsonify
from .logic import reset_game, add_player, generate_random_number, determine_winner, game_state

random_pick_bp = Blueprint('random_pick', __name__)

@random_pick_bp.route('/join', methods=['POST'])
def join_game():
    data = request.json
    player = data.get("player")
    number = data.get("number")

    if not player or number is None:
        return jsonify({"error": "Você precisa fornecer o nome do jogador e um número entre 1 e 10."}), 400

    try:
        add_player(player, number)
        return jsonify({"message": f"{player} escolheu o número {number}."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@random_pick_bp.route('/start', methods=['POST'])
def start_game():
    if not game_state["players"]:
        return jsonify({"error": "Nenhum jogador foi adicionado ao jogo."}), 400

    generate_random_number()
    random_number = game_state["random_number"]
    winners = determine_winner()

    return jsonify({
        "random_number": random_number,
        "winners": winners,
        "players": game_state["players"]
    })

@random_pick_bp.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return jsonify({"message": "O jogo foi reiniciado."})
