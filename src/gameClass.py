from conf import player
from conf import board
from conf import prompt
from conf import win_games
from random import choice
import sys

class Game:
    def __init__(self):
        self.playing = True
        self.final_state = ''
        self.pos = dict(row=0, col=0)

        # Se escoge aleatoriamente el jugador del primer turno
        self.current_player = choice(list(player.values()))

        # Variable para guardar la entrada por teclado
        self.entry = ''

        self.states = [
            'draw',
            'win player 1',
            'win player 2']

        print("modeled..")

    # Metodo para hacer un movimiento en el juego
    def accept_input(self):
        self.entry = input(f"{prompt} ")
        
        #check if is not exit
        if not (self.entry == 'exit'):
            entry = self.entry.split()

            # catch the pos entry
            self.pos['row'] = int(entry[0]) - 1
            self.pos['col'] = int(entry[1]) - 1
        
        print("input accepted.....")

    def control(self):
        # exit command check
        if self.entry == 'exit':
            sys.exit()
        
        # change symbol at entry pos
        board[self.pos['row']][self.pos['col']] = self.current_player

        # check if the current player won
        if self.win(self.current_player):
            self.playing = False
            
            # TODO: I really need this?
            self.final_state = self.states[1]

            # showing the las move
            self.default_view(self.current_player)

        # TODO: Bug1 no se dispara el evento cuando hay un juego empatado draw
        # check for draw
        count = 0
        for row in board:
            if row.count('*') == 0 and self.final_state == '':
                count+=1
            if count == 3:
                self.final_state = self.states[0]
                self.playing = False

        if self.entry == 'bye':
            self.playing = False

        # Turn controler
        if self.current_player == player['1']:
            self.current_player = player['2']
        else:
            self.current_player = player['1']

        print("controlled..")

    def view(self):
        # TODO: 
        # - Do a better view for the board check
        # - Do a view for winner state of player 1 and player 2
        # - Do a view for draw state
        
        self.default_view(self.current_player)
        
        print("viewed..")

    def win(self, player):
        """
            win(str) -> bool
            Asserts if the player from input won.
        """
        for win_game in win_games:
            count = 0
            for i in win_game:
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
