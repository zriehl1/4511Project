class Piece:

    pos = None
    color = None
    char = None
    board = None
    dynamic = False
    moves = []

    def __init__(self, board, pos, color, char):
        self.color = color
        self.pos = pos
        self.char = char
        self.board = board

    def _straightMoves(self):
        return [(0,1),(1,0),(0,-1),(-1,0)]

    def _diagonalMoves(self):
        return [(1,1),(-1,1),(1,-1),(-1,-1)]

    def _multiplyPos(self, pos, mult):
        return (pos[0] * mult, pos[1] * mult)

    def buildMoveSet(self):
        raise NotImplementedError

    def getValidPositions(self):
        raise NotImplementedError

    def canAttack(self, pos):
        if pos in self.getValidPositions():
            return True
        return False

    def getPos(self):
        return self.pos

    def getColor(self):
        return self.color

    def getChar(self):
        return self.char

    def __str__(self):
        return self.color[0] + self.char
