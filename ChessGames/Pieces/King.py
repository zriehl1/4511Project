try:
    from Piece import Piece
except:
    from .Piece import Piece

class King(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "K")
        self.buildMoveSet()

    def buildMoveSet(self):
        self.moves = []
        self.moves += self._straightMoves()
        self.moves += self._diagonalMoves()

    def getValidPositions(self):
        guardColor = "White"
        if self.getColor() == "White":
            guardColor = "Black"
        final = []
        for move in self.moves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            piece = self.board.isOccupied(new_pos)
            if piece == None:
                continue
            if not self.board.isGuarded(new_pos, guardColor) and piece.getColor() != self.getColor():
                final.append(new_pos)
        return final