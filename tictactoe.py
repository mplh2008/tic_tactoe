from Game import Game   

if __name__ == '__main__':
    game = Game()
    winner = game.play_game()
    print("{} has won!".format(winner))
