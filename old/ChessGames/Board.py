# board[0][0] is bottom left, white is bottom, black is top
# ' ' is unoccupied
from Pieces.AllPieces import Blank
class Board:

    x_dim = None
    y_dim = None
    board = None
    black = None
    white = None
    
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.black = []
        self.white = []
        self.board = [[None for i in range(y_dim)] for i in range(x_dim)]

    #adds piece to list and places pieces in starting spots
    def add_piece(self, piece):
        if piece.getColor() == "Black":
            self.black.append(piece)
        else:
            self.white.append(piece)
        x,y = piece.getPosition()
        self.board[x][y] = piece

    #put blank pieces where there arent play pieces
    def fill_blanks(self):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.board[i][j]:
                    continue
                self.board[i][j] = Blank(self, i, j, None)
    def print_board(self):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                print(self.board[self.x_dim - (i+1)][j], end = ' ')
            print('')
            
    # returns (status, piece)
    # -1 for error, 0 for not occupied, 1 for occupied
    def is_occupied(self, x, y):
        if x >= self.x_dim or x < 0:
            return (-1, None)
        if y >= self.y_dim or y < 0:
            return (-1, None)
        if self.board[x][y].__str__() == " ":
            return (0, None)
        return (1, self.board[x][y])

    # is the space guarded by a <color> piece
    def is_guarded(self, x, y, color):
        pass
    
    def captured_piece(self, piece, color):
        pass

    # move piece from current to x,y
    def move_piece(self, piece, x, y):
        pass

    # return a copy of the board
    def copy(self):
        pass
        
        
