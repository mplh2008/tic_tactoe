""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.matrix = [[None for _ in range(3)] for _ in range(3)]

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """

        self.matrix[row][column] = player

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: winner (X/O) of the game, None if no winner
        """
        for i in range(3):
            # Check Row
            if(self.matrix[i][0] == self.matrix[i][1] and self.matrix[i][2] == self.matrix[i][1]):
                return self.matrix[i][0]
            # Check Col
            if(self.matrix[0][i] == self.matrix[1][i] and self.matrix[2][i] == self.matrix[1][i]):
                return self.matrix[0][i]

        # Check Diagonals
        if(self.matrix[0][0] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][2]):
            return self.matrix[0][0]
        if(self.matrix[0][2] == self.matrix[1][1] and self.matrix[1][1] == self.matrix[2][0]):
            return self.matrix[0][2]

        return None

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """

        winner = None
        last_player = None
        plays = 0
        while(winner is None and plays < 9):
            # To do: clean the string better
            inputArr = input("Enter (column, row, player):").split(',')
            column = int(inputArr[0])
            row = int(inputArr[1])
            player = inputArr[2]
            if last_player == player:
                print("Players must switch off! Last played: {}".format(player))
            if (column > 2 or column < 0) or (row > 2 or row < 0):
                print("Position not in bounds! Enter again.")
                continue
            if self.matrix[row][column] is not None:
                self.mark_square(column, row, player)
                last_player = player
                plays += 1
            else:
                print("Square already filled! Enter again.")
                continue
            winner = self.has_winner()
        return winner
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
