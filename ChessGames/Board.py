# board[0][0] is bottom left, white is bottom, black is top
# ' ' is unoccupied
class Board:

    x_dim = None
    y_dim = None
    board = None
    black = None
    white = None
    
    def init(self, x_dim, y_dim, b_pieces, w_pieces):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.black = b_pieces
        self.white = w_pieces
        self.board = [[None for i in range(y_dim)] for i in range(x_dim)]

    def print_board(self):
        for i in range(x_dim):
            for j in range(y_dim):
                print(self.board[x_dim - (i+1)][j], end = ' ')
            print('')
            
    # returns (status, piece)
    # -1 for error, 0 for not occupied, 1 for occupied
    def is_occupied(self, x, y):
        if x >= self.x_dim or x < 0:
            return (-1, None)
        if y >= self.y_dim or y < 0:
            return (-1, None)
        if board[x][y].__str__() == " ":
            return (0, None, None)
        return (1, board[x][y])

    def is_guarded(self, x, y):
        pass
    
    def captured_piece(self, piece, color):
        pass
                      
        
        
