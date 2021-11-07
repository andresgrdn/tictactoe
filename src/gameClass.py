from conf import player
from conf import board
from conf import prompt
from random import choice
import sys

class Game:
    def __init__(self):
        self.playing = True
        self.final_state = ''
        self.pos = dict(row=0, col=0)

        # Se escoge aleatoriamente el jugador del primer turno
        self.turn = choice(list(player.values()))

        # Variable para guardar la entrada por teclado
        self.entry = ''

        self.states = [
            'draw',
            'win player 1',
            'win player 2']
        
        # All the win games
        self.win_checks = [
            [(r, 0) for r in range(3)],
            [(r, 1) for r in range(3)],
            [(r, 2) for r in range(3)],

            [(0, c) for c in range(3)],
            [(1, c) for c in range(3)],
            [(2, c) for c in range(3)],

            [(i, i) for i in range(3)],

            [(i, 2 - i) for i in range(3)]
        ]
        print("modeled..")

    # Metodo para hacer un movimiento en el juego
    def accept_input(self):
        self.entry = input(f"{prompt} ")
        
        #check if is not exit
        if not (self.entry == 'exit'):
            entry = self.entry.split()

            # catch the pos entry
            self.pos['row'] = int(entry[0])
            self.pos['col'] = int(entry[1])
        
        print("input accepted.....")
        print(f'{self.pos}')

    def control(self):
        # TODO: Do something with the input.. here

        # exit command check
        if self.entry == 'exit':
            sys.exit()

        # check if someone win
        for playr, simbolo in player.items():
            if self.win(simbolo):
                self.playing = False
                self.final_state = self.states[playr]

        # check for draw
        if board.count('*') == 0 and not (self.final_state == ''):
            self.final_state = self.states[0]
            self.playing = False

        if self.entry == 'bye':
            self.playing = False

        # Turn controler
        if self.turn == player['1']:
            self.turn = player['2']
        else:
            self.turn = player['1']

        print("controlled..")

    def view(self):
        # TODO: 
        # - Do a better view for the board check
        # - Do a view for winner state of player 1 and player 2
        # - Do a view for draw state
        if self.turn == player['1']: # if player 1 turn
            self.default_view(player['1'])
        elif self.turn == player['2']: # if player 2 turn
            self.default_view(player['2'])
        
        print("viewed..")

    def win(self, player):
        """
            win(str) -> bool
            Asserts if the player from input won.
        """
        for win_game in self.win_checks:
            for i in win_game:
                count = 0
                # (row, column) to check on board
                if board[i[0]][i[1]] == player:
                    count+=1
            if count == 3: return True
        return False

    # Gui de texto del juego, un monton de prints ;D
    def default_view(self, player):
        print(f"\
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
            \n\t")
