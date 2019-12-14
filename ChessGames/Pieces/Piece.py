# piece definitions for Pawn, Knight, Bishop, Rook, King
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

    def getPosition(self):
        return (self.cur_x, self.cur_y)

    # this function won't work for King or Pawn 
    def build_board_states(self, posList):
        for position in posList:
            

    def __str__(self):
        return char

class Blank(Piece):
    def __init__(self, board, start_x, start_y, color):
        super().__init__(board, start_x, start_y, color, " ")

    def getAllMoves(self):
        return []
    

            



        

        
    

    
