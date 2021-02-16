import unittest
from tictactoe import *

class MarkSquareTests(unittest.TestCase):

    def test_mark_square_successful(self):
        test_matrix = [[None for _ in range(3)] for _ in range(3)]
        test_matrix[0][0] = "X"
        test_board = Board()
        test_board.mark_square(0, 0, "X")
        self.assertEqual(test_matrix, test_board.matrix)


class HasWinnerTests(unittest.TestCase):

    def test_has_winner_empty_board(self):
        empty_board = Board()
        # assert that fxn call returns None
        self.assertIsNone(empty_board.has_winner())

    #full row, full col, full diag, no-win/tie, overwrite

    def test_has_winner_full_row(self):
        # fill in first row with X
        test_board = Board()
        for i in range(3):
            test_board.matrix[i][0] = "X"
        self.assertEqual(test_board.has_winner(), "X")

    def test_has_winner_full_col(self):
        # fill in first row with X
        test_board = Board()
        for i in range(3):
            test_board.matrix[0][i] = "X"
        self.assertEqual(test_board.has_winner(), "X")

        
    def test_has_winner_diag(self):

        # Arrange
        game = Board()
        game.mark_square(0,0,"X")
        game.mark_square(0,1, "O")
        game.mark_square(1,1,"X")
        game.mark_square(2,1, "O")
        game.mark_square(2,2,"X")
        '''
        [X - -]
        [O X O]
        [- - X]
        '''

        # Act
        winner = game.has_winner()

        # Assert
        self.assertEqual("X", winner)

    def test_has_winner_tie(self):

        # Arrange
        game = Board()
        game.mark_square(0,0,"X")
        game.mark_square(0,1, "O")
        game.mark_square(0,2,"X")
        game.mark_square(1,0, "X")
        game.mark_square(1,1,"O")
        game.mark_square(1,2, "X")
        game.mark_square(2,0,"O")
        game.mark_square(2,1, "X")
        game.mark_square(2,2,"O")
        '''
        [X X O]
        [O O X]
        [X X O]
        '''

        # Act
        winner = game.has_winner()

        # Assert
        self.assertIsNone(winner)

'''
    def test_has_winner_full_col(self):
        # fill in leftmost col with X
        test_board = Board()
'''
if __name__ == "__main__":
    unittest.main()
