from Pieces.AllPieces import Blank
'''
(0,0) is the bottom left of the board, with x taking you to the right and y taking you up
'''

class Board:

    def __init__(self, x, y):
        self.x_dim = x
        self.y_dim = y
        self.board = [[None for i in range(y)] for i in range(x)]
        self.black = []
        self.white = []

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
        return True

    def addPiece(self, piece):
        if piece.getColor() == "Black":
            self.black.append(piece)
        elif piece.getColor() == "White":
            self.white.append(piece)
        pos = piece.getPos()
        self.board[pos[0]][pos[1]] = piece

    def fillBlanks(self):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.board[i][j] == None:
                    self.board[i][j] = Blank(self, (i,j), "-")

    # returns the piece at the position
    def isOccupied(self, pos):
        if not self.checkBounds(pos):
            return None
        return self.board[pos[0]][pos[1]]

    # see if the position is guarded by the color
    # ignores whether the king is guarding the position, otherwise it loops infinately
    def isGuarded(self, pos, color):
        if color == "White":
            for el in self.white:
                if el.getChar() == "K":
                    guarded = el.getSpaceAround()
                    if pos in guarded:
                        return True
                    continue
                if el.canAttack(pos):
                    return True
            return False
        elif color == "Black":
            for el in self.black:
                if el.getChar() == "K":
                    guarded = el.getSpaceAround()
                    if pos in guarded:
                        return True
                    continue
                if el.canAttack(pos):
                    return True
            return False

    # returns whether the colors king is in check
    def checkKing(self, color):
        color_pieces = None
        other_color = None
        king = None
        if color == "White":
            color_pieces = self.white
            other_color = "Black"
        else:
            color_pieces = self.black
            other_color = "White"
        for el in color_pieces:
            if el.getChar() == "K":
                king = el
        return self.isGuarded(king.getPos(), other_color)

    def isCheckmate(self, color):
        king = None
        pieces = None
        attacking = None
        if color == "White":
            pieces = self.white
            attacking = self.black
        else:
            pieces = self.black
            attacking = self.white
        for el in pieces:
            if el.getChar() == "K":
                king = el
        if self.checkKing(color) and king.getValidPositions() == []:
            # also have to check that the checkmate cant be blocked
            return True
        return False


    # remove a piece from the game
    def capturePiece(self, piece):
        if piece.getChar() == " ":
            return
        rem = self.white
        if piece.getColor() == "Black":
            rem = self.black
        rem.remove(piece)

    # returns True on sucessful move, False on failure
    def movePiece(self, start, to):
        piece = self.board[start[0]][start[1]]
        if to not in piece.getValidPositions():
            print("Not a valid move.")
            return False
        captured = self.board[to[0]][to[1]]
        isCheck = self.checkKing(piece.getColor())
        if isCheck and piece.getChar() != "K":
            print("Can't move this, you're in check.")
            return False
        self.board[to[0]][to[1]] = piece
        self.board[start[0]][start[1]] = Blank(self, (start[0],start[1]), "-")
        piece.setPos(to)
        isCheck2 = self.checkKing(piece.getColor())
        if isCheck2:
            self.board[to[0]][to[1]] = captured
            self.board[start[0]][start[1]] = piece
            piece.setPos(start)
            print("Can't move this. The move is pinned.")
            return False
        piece.moved = True
        self.capturePiece(captured)

        return True




























#
