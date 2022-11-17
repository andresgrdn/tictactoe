from conf import (
    PLAYERS,
    QUIT_CMDS,
    board,
    PROMPT,
    WIN_RULES,
    State,
)
from random import choice
from sys import exit


class Game:

    def __init__(self):
        self.setup()
        print("modeled..")

    def setup(self) -> None:
        self.playing = True
        self.game_state: State = State.NONE
        self.pos = [0, 0]

        self.current_player = choice(PLAYERS)

        self.input_cmd = ''

    def parse_input(self):
        self.input_cmd = input(f"{PROMPT} ")

        if self.input_cmd in QUIT_CMDS:
            exit()

        tokens: list[str] = self.input_cmd.split()

        self.pos = [
            int(tokens[0]) - 1,
            int(tokens[1]) - 1,
        ]

        print("input parsed.....")

    def control(self):
        self._change_slot(self.pos, self.current_player)

        current_player_win: bool = self._is_winner(self.current_player)
        game_draw: bool = (
            board.count('*') == 0 and
            not (self.game_state == State.WIN)
        )

        if game_draw:
            self.playing = False
            self.game_state = State.DRAW
            self.update_view()

        if current_player_win:
            self.playing = False
            self.game_state = State.WIN
            self.update_view()

        # Turn
        self.current_player = PLAYERS[1] if (
            self.current_player == PLAYERS[0]
        ) else PLAYERS[0]

        print("Controlled...")

    def update_view(self):
        if self.game_state == State.DRAW:
            self.show_draw()
        elif self.game_state == State.WIN:
            self.show_winner(self.current_player)
        else:
            self.show_layout(self.current_player)

    def _is_winner(self, player: str) -> bool:
        winner: bool = False

        for rule in WIN_RULES:
            points: int = 0
            for pos in rule:
                [row, column] = pos
                if board[row][column] == player:
                    points += 1

            has_win_points: bool = points == 3
            if has_win_points:
                winner = True

        return winner

    def show_layout(self, player: str) -> None:
        layout = f"\
            \n\t ********* PLAYER {player} *********\
            \n\
            \n\t\t    1   2   3\
            \n\
            \n\t\t 1  {board[0][0]} | {board[0][1]} | {board[0][2]}\
            \n\t\t    ----------\
            \n\t\t 2  {board[1][0]} | {board[1][1]} | {board[1][2]}\
            \n\t\t    ----------\
            \n\t\t 3  {board[2][0]} | {board[2][1]} | {board[2][2]}\
            \n\
            \n\t"

        print(layout)

    def show_winner(self, player: str) -> None:
        layout = f"\
            \n\t ********* WIN PLAYER {player} *********\
            \n\
            \n\t\t    1   2   3\
            \n\
            \n\t\t 1  {board[0][0]} | {board[0][1]} | {board[0][2]}\
            \n\t\t    ----------\
            \n\t\t 2  {board[1][0]} | {board[1][1]} | {board[1][2]}\
            \n\t\t    ----------\
            \n\t\t 3  {board[2][0]} | {board[2][1]} | {board[2][2]}\
            \n\
            \n\t"

        print(layout)

    def show_draw(self) -> None:
        layout = f"\
            \n\t ********* GAME OVER *********\
            \n\t *********    DRAW   *********\
            \n\
            \n\t\t    1   2   3\
            \n\
            \n\t\t 1  {board[0][0]} | {board[0][1]} | {board[0][2]}\
            \n\t\t    ----------\
            \n\t\t 2  {board[1][0]} | {board[1][1]} | {board[1][2]}\
            \n\t\t    ----------\
            \n\t\t 3  {board[2][0]} | {board[2][1]} | {board[2][2]}\
            \n\
            \n\t"

        print(layout)

    def _change_slot(self, pos: list[int], symbol: str) -> None:
        [row, col] = pos
        board[row][col] = symbol
