from src import *

def main():
    myGame = Game()

    while myGame.playing:
        myGame.view()
        myGame.accept_input()
        myGame.control()

if __name__ == '__main__':
    main()