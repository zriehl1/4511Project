try:
    from Piece import Piece
    from Blank import Blank
except:
    from .Piece import Piece
    from .Blank import Blank
    
class King(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "K")
        self.buildMoveSet()

    def buildMoveSet(self):
        self.moves = []
        self.moves += self._straightMoves()
        self.moves += self._diagonalMoves()

    def getSpaceAround(self):
        final = []
        for el in self.moves:
            final.append((el[0] + self.pos[0], el[1] + self.pos[1]))
        return final

    def getValidPositions(self):
        guardColor = "White"
        if self.getColor() == "White":
            guardColor = "Black"
        final = []
        self.board.board[self.pos[0]][self.pos[1]] = Blank(self.board, self.pos, " ")
        for move in self.moves:
            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            piece = self.board.isOccupied(new_pos)
            if piece == None:
                continue
            if not self.board.isGuarded(new_pos, guardColor) and piece.getColor() != self.getColor():
                final.append(new_pos)
        self.board.board[self.pos[0]][self.pos[1]] = self
        return final

    def getGuards(self):
        return self.getSpaceAround()
