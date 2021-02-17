import unittest
from unittest.mock import patch
from Game import *
from Player import *

class MarkSquareTests(unittest.TestCase):

    def test_mark_square_successful(self):

        # Make a board
        test_matrix = [[None for _ in range(3)] for _ in range(3)]
        test_matrix[0][0] = "X"

        playerX = Player("X")

        test_board = Game()
        test_board.mark_square(0, 0, playerX)
        self.assertEqual(test_matrix, test_board.board)
    

class HasWinnerTests(unittest.TestCase):
    
    def test_has_winner_diag(self):
    
        # Arrange
        game = Game()

        playerX = Player("X")
        playerO = Player("O")

        game.mark_square(0,0,playerX)
        game.mark_square(0,1,playerO)
        game.mark_square(1,1,playerX)
        game.mark_square(2,1,playerO)
        game.mark_square(2,2,playerX)
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
        game = Game()
        
        playerX = Player("X")
        playerO = Player("O")
        
        game.mark_square(0,0,playerX)
        game.mark_square(0,1,playerO)
        game.mark_square(0,2,playerX)
        game.mark_square(1,0,playerX)
        game.mark_square(1,1,playerO)
        game.mark_square(1,2,playerX)
        game.mark_square(2,0,playerO)
        game.mark_square(2,1,playerX)
        game.mark_square(2,2,playerO)
        '''
        [X X O]
        [O O X]
        [X X O]
        '''

        # Act
        winner = game.has_winner()

        # Assert
        self.assertIsNone(winner)

class play_game(unittest.TestCase):
    
    # Branch testing for bounds
    @patch('Game.input', return_value='5,0')    
    def test_inputs_out_of_bounds_ro(self, input):
        game = Game()
        with self.assertRaises(Exception): game.play_game()

    @patch('Game.input', return_value='1,7')    
    def test_inputs_out_of_bounds_col(self, input):
        game = Game()
        with self.assertRaises(Exception): game.play_game()

    @patch('Game.input', return_value='7,7')    
    def test_inputs_out_of_bounds_both(self, input):
        game = Game()
        with self.assertRaises(Exception): game.play_game()

    @patch('Game.input', return_value='0,0')    
    def test_inputs_already_marked(self, input):
        game = Game()
        game.board[0][0] = "X"
        with self.assertRaises(Exception): game.play_game()


    #check valid play_game()
    '''
    [X - -]
    [O X O]
    [- - X]
    '''
    @patch('Game.input', side_effects=['0,0', '0,1', '1,1', '2,1', '2,2'])
    # @patch('Game.input2', return_value='0,1') 
    # @patch('Game.input3', return_value='1,1')
    # @patch('Game.input4', return_value='2,1')
    # @patch('Game.input5', return_value='2,2')
    #def test_inputs_valid(self, input, input2, input3, input4, input5):
    def test_inputs_valid(self, side_effects):
        game = Game()
        playerX = Player("X")
        playerO = Player("O")

        for x in side_effects:
            winner = game.play_game()
            self.assertEqual("X", winner)


if __name__ == "__main__":
    unittest.main()