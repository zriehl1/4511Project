# piece definitions for Pawn, Knight, Bishop, Rook, King
class Piece:

    board = None
    cur_x = None
    cur_y = None
    char = None
    color = None

    def __init__(self, board, start_x, start_y, color, char):
        self.board = board
        self.cur_x = start_x
        self.cur_y = start_y
        self.char = color[0] + char
        self.color = color

    def getAllMoves(self):
        raise NotImplementedError

    def getPosition(self):
        return (self.cur_x, self.cur_y)

    def getColor(self):
        return self.color

    # this function won't work for Pawn 
    def getPositions(self, posList):
        allowed_positions = []
        for position in posList:
            new_pos = (self.cur_x + position[0], self.cur_y + position[1])
            tile_info = self.board.is_occupied(new_pos[0], new_pos[1])
            if tile_info[0] == -1:
                continue
            elif tile_info[1].getColor() == self.getColor():
                continue
            elif self.char == 'K':
                if self.board.is_guarded(new_pos[0], new_pos[1]):
                    continue
            else:
                allowed_positions.append(new_pos)
        return allowed_positions
            

    def __str__(self):
        return self.char

class Blank(Piece):
    def __init__(self, board, start_x, start_y, color):
        super().__init__(board, start_x, start_y, "-", " ")

    def getAllMoves(self):
        return []
    

            



        

        
    

    
