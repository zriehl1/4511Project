try:
    from .Piece import Piece
except:
    from Piece import Piece
    
class Bishop(Piece):

    possible_moves = []
    
    def __init__(self, board, start_x, start_y, color):
        super().__init__(board, start_x, start_y, color, "B")
        self.__set_possible_moves()

    def __set_possible_moves(self):
        bsize = max(self.board.x_dim, self.board.y_dim)
        for i in range(0, bsize+1):
            if i != 0:
                self.possible_moves.append((i,i))
                self.possible_moves.append((-i,i))
                self.possible_moves.append((i,-i))
                self.possible_moves.append((-i,-i))
