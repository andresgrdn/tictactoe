from os import system

class Game: # TODO implement
    def __init__(self):
        self.model()

    def model(self):
        self.playing = True
        self.final_state = ''

        self.player1 = "X"
        self.player2 = "O"

        self.board = ['*' for row in range(3) for col in range(3)]

        self.states = [
            'draw',
            'win player 1',
            'win player 2']
        
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
        self.entry = input( "*- ")

        # for win_state in win_checks:
        #     for coor in win_state:
        #         if self.board[coor]

        # TODO:
        # - Implement player 1 and 2 win check
        # - Implement board checker
        
        if self.board.count('*') == 0 and self.final_state != '':
            # draw state
            self.final_state = self.states[0]
            self.playing = False

        if self.entry == 'bye':
            self.playing = False

        print("controlled..")

    def view(self):
        print("viewed..")