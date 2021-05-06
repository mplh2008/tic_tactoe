class Player():
    def __init__(self, playerId):
        self.playerId = playerId

    def make_move(self, board, row, col):
        # check if valid
        if(row < 0 or row > 2):
            raise RuntimeError("Outside row bounds!")
        if(col < 0 or col > 2):
            raise RuntimeError("Outside col bounds!")
        if(board[row][col] is not None):  # pragma: no cover
            raise RuntimeError("Illegal Move! Position already marked with {}".format(board[row][col]))

        board[row][col] = self.playerId
