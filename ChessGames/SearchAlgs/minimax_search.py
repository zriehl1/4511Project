#sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
try:
    from heuristic import *
except:
    from .heuristic import *

class MinimaxNode:

    def __init__(self, board, color, depth, turn=0):
        self.color = color
        self.board = board
        self.type = turn % 2 # max node if 0, min node if 1
        self.children = []
        self.invalid = []
        self.value = None
        if depth == 0:
            self.value = calculateHeuristic(self.board, color)
            return
        child_boards = self.makeChildBoards(color, turn)
        for el in child_boards:
            self.children.append(MinimaxNode(el, color, depth-1, turn+1))

    def makeChildBoards(self, color, turn):
        ret = []
        pieces = None
        if (color == "Black" and turn % 2 == 0) or (color == "White" and turn % 2 == 1):
            pieces = self.board.black
        else:
            pieces = self.board.white
        for piece in pieces:
            possible = piece.getValidPositions()
            for move in possible:
                newBoard = self.board.copy()
                valid = newBoard.movePiece(piece.getPos(), move, True)
                if valid:
                    ret.append(newBoard)
        return ret

    def printTree(self, depth=0):
        print("Depth: " + str(depth) + " Value: " + str(self.value))
        self.board.printBoard()
        print("------------------------------")
        for el in self.children:
            el.printTree(depth+1)

    def getMove(self):
        values = []
        for child in self.children:
            values.append(child.getValue())
        _max = max(values)
        for el in self.children:
            if _max == el.getValue() and el not in self.invalid:
                self.invalid.append(el.board)
                return el.board.lastMove

    def getValue(self):
        child_vals = []
        if self.value != None:
            return self.value
        if len(self.children) == 0:
            self.value = calculateHeuristic(self.board, self.color)
            return self.value
        if self.type == 0:
            for child in self.children:
                child_vals.append(child.getValue())
            self.value = max(child_vals)
        elif self.type == 1:
            for child in self.children:
                child_vals.append(child.getValue())
            self.value = min(child_vals)
        return self.value
