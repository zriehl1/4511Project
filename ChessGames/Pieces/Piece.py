class Piece:

    def __init__(self, board, pos, color, char):
        self.moved = False
        self.color = color
        self.pos = pos
        self.char = char
        self.board = board
        self.moves = []

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

    def getGuards(self, pos):
        raise NotImplementedError

    def canAttack(self, pos):
        positions = self.getValidPositions()
        if pos in positions:
            return self
        return False

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getColor(self):
        return self.color

    def getChar(self):
        return self.char

    def __str__(self):
        return self.color[0] + self.char
