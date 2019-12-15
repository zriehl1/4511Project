try:
    from Piece import Piece
except:
    from .Piece import Piece

class Blank(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, " ")
        self.buildMoveSet()

    #populate moves with all possible x,y additions
    def buildMoveSet(self):
        self.moves = []

    def getValidPositions(self):
        return []
