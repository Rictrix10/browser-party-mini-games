def init_game():
    return {
        "board": [["" for _ in range(7)] for _ in range(6)],  # Tabuleiro 6x7
        "winner": None,
    }

def check_winner(board):
    # Verifica linhas
    for row in board:
        for col in range(len(row) - 3):
            if row[col] and row[col] == row[col + 1] == row[col + 2] == row[col + 3]:
                return row[col]

    # Verifica colunas
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if board[row][col] and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return board[row][col]

    # Verifica diagonais (\)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]

    # Verifica diagonais (/)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if board[row][col] and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]

    return None

def make_move(game_state, username, row, col):
    if game_state["winner"]:
        raise ValueError("Game already has a winner.")

    if row < 0 or row >= len(game_state["board"]) or col < 0 or col >= len(game_state["board"][0]):
        raise ValueError("Invalid row or column.")

    if game_state["board"][row][col]:
        raise ValueError("Cell already occupied.")

    # Atualiza o tabuleiro
    game_state["board"][row][col] = username

    # Verifica se há vencedor
    winner = check_winner(game_state["board"])
    if winner:
        game_state["winner"] = winner

    return game_state["board"], game_state["winner"]

def reset_game(game_state):
    game_state["board"] = [["" for _ in range(7)] for _ in range(6)]
    game_state["winner"] = None
