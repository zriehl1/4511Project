try:
    from .Piece import Piece
except:
    from Piece import Piece
    
class Knight(Piece):
    # right up, right down, left up, left down, up right, up left, down right, down left
    possible_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    def __init__(self, board, start_x, start_y, color):
        super().__init__(board, start_x, start_y, color, "H")
