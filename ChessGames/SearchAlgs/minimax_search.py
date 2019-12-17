try:
    from heuristic import *
except:
    .from heuristic import *

class MinimaxNode:

    def __init__(self, board, color, depth, turn=0):
        self.board = board
        self.type = turn % 2 # max node if 0, min node if 1
        self.children = []
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
        else color == "Black":
            pieces = self.board.white
        for piece in pieces:
            possible = piece.getValidPositions()
            for move in possible:
                newBoard = self.board.copy()
                newBoard.movePiece(piece.getPos(), move)
                ret.append(newBoard)
        return ret
# build a minimax tree of depth <depth>, starting from board, from <color>'s perspective
