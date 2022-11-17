from enum import (
    Enum,
    auto,
)


PROMPT = '>>'
PLAYERS = ['x', 'y']
WIN_RULES = [
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
board = [['*' for col in range(3)] for row in range(3)]
# ['X', 'O', 'O']
# ['*', 'X', '*']
# ['*', '*', 'x']
QUIT_CMDS: list[str] = [
    'exit',
    'bye'
]


class State(Enum):
    DRAW = auto(),
    WIN = auto(),
    NONE = auto(),
