try:
    from heuristic import *
except:
    .from heuristic import *

class MinimaxNode:

    def __init__(self, board, turn, color, depth, max=True):
        self.board = board
        self.children = self.makeChildren(turn)

    def makeChildren(self, color):
        pass
# build a minimax tree of depth <depth>, starting from board, from <color>'s perspective
