try:
    from Piece import Piece
except:
    from .Piece import Piece

class Rook(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "R")
        self.buildMoveSet()

    #populate moves with all possible x,y additions
    def buildMoveSet(self):
        self.moves = self._straightMoves()

    def getValidPositions(self):
        max_dist = max(self.board.x_dim, self.board.y_dim)
        final = []
        done = False
        for move in self.moves:
            for i in range(max_dist+1):
                if i == 0 or done:
                    continue
                new_pos = self._multiplyPos(move, i)
                piece = self.board.isOccupied(new_pos)
                if piece == None or piece.getColor() == self.getColor():
                    done = True
                else:
                    final.append(new_pos)
