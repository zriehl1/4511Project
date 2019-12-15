try:
    from Piece import Piece
except:
    from .Piece import Piece

class Knight(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "H")
        self.buildMoveSet()

    #populate moves with all possible x,y additions
    def buildMoveSet(self):
        self.moves.append((1,2))
        self.moves.append((2,1))
        self.moves.append((-1,2))
        self.moves.append((2,-1))
        self.moves.append((1,-2))
        self.moves.append((-2,1))
        self.moves.append((-1,-2))
        self.moves.append((-2,-1))

    def getValidPositions(self):
        final = []
        for move in self.moves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            piece = self.board.isOccupied(new_pos)
            if piece == None:
                continue
            if piece.getColor() != self.getColor():
                final.append(new_pos)
