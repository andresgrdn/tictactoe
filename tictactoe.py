from src import Game


def main():
    myGame = Game()

    while myGame.playing:
        myGame.update_view()
        myGame.parse_input()
        myGame.update_game()


if __name__ == '__main__':
    main()
