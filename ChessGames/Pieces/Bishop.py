try:
    from Piece import Piece
except:
    from .Piece import Piece

class Bishop(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "B")
        self.buildMoveSet()

    #populate moves with all possible x,y additions
    def buildMoveSet(self):
        self.moves = self._diagonalMoves()

    def copyWithBoard(self, board):
        return Bishop(board, self.getPos(), self.getColor())
        
    def getValidPositions(self):
        max_dist = max(self.board.x_dim, self.board.y_dim)
        final = []
        done = False
        for move in self.moves:
            done = False
            for i in range(max_dist+1):
                if i == 0 or done:
                    continue
                add = self._multiplyPos(move, i)
                new_pos = (self.pos[0] + add[0], self.pos[1] + add[1])
                piece = self.board.isOccupied(new_pos)
                if piece == None or piece.getColor() == self.getColor():
                    done = True
                else:
                    final.append(new_pos)
                    if piece.getChar() != " ":
                        done = True
        return final

    def getGuards(self):
        max_dist = max(self.board.x_dim, self.board.y_dim)
        final = []
        done = False
        for move in self.moves:
            done = False
            for i in range(max_dist+1):
                if i == 0 or done:
                    continue
                add = self._multiplyPos(move, i)
                new_pos = (self.pos[0] + add[0], self.pos[1] + add[1])
                piece = self.board.isOccupied(new_pos)
                if piece == None:
                    done = True
                elif piece.getColor() == self.getColor():
                    final.append(new_pos)
                    done = True
                else:
                    final.append(new_pos)
                    if piece.getChar() != " ":
                        done = True
        return final
