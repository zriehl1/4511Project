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
        self.lastMove = None

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
                if pos in el.getGuards():
                    return True
            return False
        elif color == "Black":
            for el in self.black:
                if el.getChar() == "K":
                    guarded = el.getSpaceAround()
                    if pos in guarded:
                        return True
                    continue
                if pos in el.getGuards():
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

    # captures a piece, checks to see if this induces check, put it back and return the result
    def __checkCapture(self, start, end):
        attacker = self.board[start[0]][start[1]]
        captured = self.board[end[0]][end[1]]
        self.board[start[0]][start[1]] = Blank(self.board, (start[0], start[1]), " ")
        self.board[end[0]][end[1]] = attacker
        result = self.checkKing(attacker.getColor())
        self.board[start[0]][start[1]] = attacker
        self.board[end[0]][end[1]] = captured
        return result

    # assumes there is an unbroken line between the two pieces
    # ie strictly horizontal/vertical, or diagonal
    # the return doesnt include the endpoints
    def __getTilesBetween(self, start, end):
        x_vals = []
        y_vals = []
        x_step = 1
        y_step = 1
        if start[0] > end[0]:
            x_step = -1
        if start[1] > end[1]:
            y_step = -1
        for i in range(start[0], end[0], x_step):
            x_vals.append(i)
        for j in range(start[1], end[1], y_step):
            y_vals.append(j)
        if start[0] == end[0]:
            x_vals = [start[0] for i in range(len(y_vals))]
        if start[1] == end[1]:
            y_vals = [start[1] for i in range(len(x_vals))]
        ret = []
        if len(x_vals) != len(y_vals):
            print("error")
            return []
        for i in range(len(x_vals)):
            pos = (x_vals[i], y_vals[i])
            if pos != start and pos != end:
                ret.append(pos)
        return ret

    def getTiles(self, start, end):
        return self.__getTilesBetween(start, end)

    def tryBlock(self, attacker, save):
        defenders = None
        color = attacker.getColor()
        if color == "Black":
            defenders = self.white
        else:
            defenders = self.black
        # attempt to capture the piece
        for piece in defenders:
            if piece.canAttack(attacker.getPos()):
                if self.__checkCapture(piece.getPos(), attacker.getPos()):
                    return True
        if attacker.getChar() == "H": # if you cant capture the Knight, you can't block it
            return False
        tiles = self.__getTilesBetween(attacker.getPos(), save.getPos())
        for tile in tiles:
            for piece in defenders:
                if piece.canAttack(tile):
                    if self.__checkCapture(piece.getPos(), tile):
                        return True
        return False
    # this function won't work perfectly, will miss checkmate if you can move a pinned piece to block check
    # this should get picked up by the game, since it won't actually let you move the piece
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
            to_block = []
            for piece in attacking:
                if piece.canAttack(king.getPos()):
                    to_block.append(piece)
            if len(to_block) > 1:
                return True
            return not self.tryBlock(piece, king)
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
    def movePiece(self, start, to, bot=False):
        piece = self.board[start[0]][start[1]]
        if to not in piece.getValidPositions():
            if not bot:
                print("Not a valid move.")
            return False
        captured = self.board[to[0]][to[1]]
        # isCheck = self.checkKing(piece.getColor())
        # if isCheck and piece.getChar() != "K":
        #     print("Can't move this, you're in check.")
        #     return False
        self.capturePiece(captured)
        self.board[to[0]][to[1]] = piece
        self.board[start[0]][start[1]] = Blank(self, (start[0],start[1]), "-")
        piece.setPos(to)
        isCheck2 = self.checkKing(piece.getColor())
        if isCheck2:
            self.addPiece(captured)
            self.board[to[0]][to[1]] = captured
            self.board[start[0]][start[1]] = piece
            piece.setPos(start)
            if not bot:
                print("Can't move this. The move is pinned.")
            return False
        piece.moved = True
        #self.capturePiece(captured)
        self.lastMove = (start, to)
        return True

    # returns a copy of itself
    def copy(self):
        ret = Board(self.x_dim, self.y_dim)
        for piece in self.white:
            ret.addPiece(piece.copyWithBoard(ret))
        for piece in self.black:
            ret.addPiece(piece.copyWithBoard(ret))
        ret.fillBlanks()
        return ret




























#
