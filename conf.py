# Prompt
prompt = '>> '

# jugadores
player = {
    '1':'X',
    '2':'O'
    }

# Construye el tablero de 3 col x 3 row
board = [['*' for col in range(3)] for row in range(3)]

# win games son las reglas para ganar
win_games = [
    # landscape win games
    [(r, 0) for r in range(3)],
    [(r, 1) for r in range(3)],
    [(r, 2) for r in range(3)],

    # Vertical win games
    [(0, c) for c in range(3)],
    [(1, c) for c in range(3)],
    [(2, c) for c in range(3)],

    # Diagonal win games
    [(i, i) for i in range(3)],
    [(i, 2 - i) for i in range(3)]
]