import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#print(os.path.dirname(os.path.dirname(__file__)))

from heuristic import *
from minimax_search import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Board import *
from Pieces.AllPieces import *

w = "White"
b = "Black"

class TestHeuristic(unittest.TestCase):

    board = None
    white = None
    black = None

    def setUp(self):
        self.board = Board(4,5)
        self.white = []
        self.black = []
        self.white.append(King(self.board, (0,0), "White"))
        self.black.append(King(self.board, (0,4), "Black"))
        for el in self.white + self.black:
            self.board.addPiece(el)
        self.board.fillBlanks()

    def test_minimax_build(self):
        print("MINIMAXBUILD 1")
        a = MinimaxNode(self.board, "White", 1)
        a.printTree()

    def test_minimax_build2(self):
        print("MINIMAXBUILD 2")
        a = MinimaxNode(self.board, "White", 2)
        a.printTree()

    def test_minimax_get_board(self):
        print("MINIMAX BOARD 1")
        a = MinimaxNode(self.board, "White", 1)
        a.getMove().printBoard()

    def test_minimax_get_board2(self):
        print("MINIMAX BOARD 2")
        a = MinimaxNode(self.board, "White", 7)
        a.getMove().printBoard()
