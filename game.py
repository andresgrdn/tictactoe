from src.gameClass import Game

def main():
    myGame = Game()

    while myGame.playing:
        myGame.control()
        myGame.view()

if __name__ == '__main__':
    main()