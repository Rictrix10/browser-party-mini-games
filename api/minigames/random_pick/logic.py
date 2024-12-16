import random

# Estado global do jogo
game_state = {
    "players": {},   # Armazena as escolhas dos jogadores
    "random_number": None,  # Número gerado
    "winner": None   # Vencedor atual
}

def reset_game():
    """Reseta o estado do jogo."""
    game_state["players"] = {}
    game_state["random_number"] = None
    game_state["winner"] = None

def add_player(player, number):
    """Adiciona ou atualiza a escolha de um jogador."""
    if number < 1 or number > 10:
        raise ValueError("O número deve estar entre 1 e 10.")
    game_state["players"][player] = number

def generate_random_number():
    """Gera o número aleatório para o jogo."""
    game_state["random_number"] = random.randint(1, 10)

def determine_winner():
    """Determina o vencedor com base na proximidade do número."""
    if not game_state["players"] or game_state["random_number"] is None:
        raise ValueError("O jogo ainda não começou ou não há jogadores.")
    
    closest_diff = float('inf')
    winners = []

    for player, number in game_state["players"].items():
        diff = abs(game_state["random_number"] - number)
        if diff < closest_diff:
            closest_diff = diff
            winners = [player]
        elif diff == closest_diff:
            winners.append(player)

    game_state["winner"] = winners
    return winners
