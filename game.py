from src.gameClass import Game

def main():
    myGame = Game()

    while myGame.playing:
        myGame.view()
        myGame.accept_input()
        myGame.control()

if __name__ == '__main__':
    main()