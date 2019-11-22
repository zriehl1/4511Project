class Piece:

    board = None
    cur_x = None
    cur_y = None
    char = None

    def __init__(self, board, start_x, start_y, color, char):
        self.board = board
        self.cur_x = start_x
        self.cur_y = start_y
        self.char = char

    def getAllMoves(self):
        raise NotImplementedError

    def __str__(self):
        return char

class Blank(Piece):
    def __init__(self, board, start_x, start_y, color):
        super.__init__(board, start_x, start_y, color " ")

    def getAllMoves(self):
        return []
    
class Pawn(Piece):

    has_moved = False

    def __init__(self, board, start_x, start_y, color):
        super.__init__(board, start_x, start_y, color, "P")

    # returns a list of new boards for every valid move by the piece
    def getAllMoves(self):
        all_moves = []
        if not self.has_moved:
            forward_2 = self.board.is_occupied(self.cur_x + 2, self.cur_y)
            if forward_2[0] == 0:
                pass # new board
        forward_1 = self.board.is_occupied(self.cur_x + 1, self.cur_y)
        if forward_1[0] == 0:
            pass # new board
        take_left = self.board.is_occupied(self.cur_x + 1, self.cur_y - 1)
        if take_left[0] == 1 and take_left[1].color != self.color:
            pass # new board
        take_right = self.board.is_occupied(self.cur_x + 1, self.cur_y + 1)
        if take_right[0] == 1 and take_right[1].color != self.color:
            pass # new board
            
        
            
        
