'''
(0,0) is the bottom left of the board, with x taking you to the right and y taking you up
'''
class Board:

    x_dim = None
    y_dim = None
    board = None
    black = []
    white = []

    def __init__(self, x, y):
        self.x_dim = x
        self.y_dim = y
        self.board = [["O" for i in range(y)] for i in range(x)]

    def printBoard(self):
        for i in range(self.y_dim-1, 0-1, -1):
            for j in range(self.x_dim):
                print(self.board[j][i], end=' ')
            print('')

    def getXDim(self):
        return self.x_dim

    def getYDim(self):
        return self.y_dim

    def checkBounds(self, pos):
        if pos[0] < 0 or pos[0] >= self.x_dim:
            return False
        if pos[1] < 0 or pos[1] >= self.y_dim:
            return False

    # returns the piece at the position
    def isOccupied(self, pos):
        if not self.checkBounds(pos):
            return None
        return self.board[pos[0]][pos[1]]

    def isGuarded(self, pos, color):
        if color == "White":
            for el in self.white:
                if el.canAttack(pos):
                    return True
            return False
        elif color == "Black":
            for el in self.black:
                if el.canAttack(pos):
                    return True
            return False
