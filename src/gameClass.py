from os import system

class Game:
    def __init__(self):
        self.model()

    def model(self):
        self.playing = True
        self.final_state = ''

        self.player1 = "X"
        self.player2 = "O"

        # TODO: Refactor at one line
        self.board = []
        for row in range(3):
            self.board.append(['*' for column in range(3)])

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

    def control(self):
        self.entry = input("*- ")

        # TODO: Do something with the input.. here

        # check if someone win
        if self.win(self.player1):
            self.playing = False
            self.final_state = self.states[1]
        
        if self.win(self.player2):
            self.playing = False
            self.final_state = self.states[2]

        # check for draw
        if self.board.count('*') == 0 and self.final_state != '':
            self.final_state = self.states[0]
            self.playing = False

        if self.entry == 'bye':
            self.playing = False

        print("controlled..")

    def view(self):
        # TODO: 
        # - Do a better view for the board
        # - Do a view for winner state of player 1 and player 2
        # - Do a view for draw state
        print(self.board)
        print("viewed..")

    def win(self, player):
        """
            win(str) -> bool
            Asserts if player from input win.
        """
        for win_game in self.win_checks:
            for i in win_game:
                count = 0
                # (row, column) to check on board
                if self.board[i[0]][i[1]] == player:
                    count+=1
            if count == 3: return True
        return False