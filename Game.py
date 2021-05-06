from Player import Player

class Game(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        Create the two players
        """
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player1 = Player("X")
        self.player2 = Player("O")

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (Player) the player

        :return: ????
        """

        player.make_move(self.board, row, column)

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: winner (X/O) of the game, None if no winner
        """
        for i in range(3):
            # Check Row
            if(self.board[i][0] == self.board[i][1] and self.board[i][2] == self.board[i][1]):
                return self.board[i][0]
            # Check Col
            if(self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i]):
                return self.board[0][i]

        # Check Diagonals
        if(self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
        if(self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]):
            return self.board[0][2]

        return None

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=" ")
            print()


    # def play_round()
    
    def play_game(self): # pragma: no cover
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends
        
        :return: (str) the letter representing the player who won
        """

        winner = None
        player1Turn = True
        plays = 0
        while(winner is None and plays < 9):
            self.print_board()

            # To do: clean the string better
            inputArr = input("Player {}'s Turn, please enter (column, row):".format(1 if player1Turn else 2)).split(',')
            column = int(inputArr[0])
            row = int(inputArr[1])

            try:
                if(player1Turn):
                    self.mark_square(column, row, self.player1)
                else:
                    self.mark_square(column, row, self.player2)
                plays += 1
                player1Turn = not player1Turn
            except Exception as e:
                raise Exception("Invalid Input: {}".format(e))

            winner = self.has_winner()
        return winner
   
