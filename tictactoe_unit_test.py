import unittest
from Game import *
from Player import *

class HasWinnerTests(unittest.TestCase):

    def test_has_winner_empty_board(self):
        empty_board = Game()
        # assert that fxn call returns None
        self.assertIsNone(empty_board.has_winner())

    #full row, full col, full diag, no-win/tie, overwrite

    def test_has_winner_full_row(self):
        # fill in first row with X
        test_board = Game()
        for i in range(3):
            test_board.board[i][0] = "X"
        self.assertEqual(test_board.has_winner(), "X")

    def test_has_winner_full_col(self):
        # fill in first row with X
        test_board = Game()
        for i in range(3):
            test_board.board[0][i] = "X"
        self.assertEqual(test_board.has_winner(), "X")

        
'''
    def test_has_winner_full_col(self):
        # fill in leftmost col with X
        test_board = Board()
'''

if __name__ == "__main__":
    unittest.main()
