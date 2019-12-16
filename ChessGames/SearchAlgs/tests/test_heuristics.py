import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#print(os.path.dirname(os.path.dirname(__file__)))

from heuristic import *

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
        self.white.append(Rook(self.board, (0,0), w))
        self.white.append(Bishop(self.board, (1,0), w))
        self.white.append(Knight(self.board, (2,0), w))
        self.white.append(King(self.board, (3,0), w))
        self.white.append(Pawn(self.board, (3,1), w))
        self.black.append(Pawn(self.board, (0,3), b))
        self.black.append(King(self.board, (0,4), b))
        self.black.append(Knight(self.board, (1,4), b))
        self.black.append(Bishop(self.board, (2,4), b))
        self.black.append(Rook(self.board, (3,4), b))
        for piece in self.black:
            self.board.addPiece(piece)
        for piece in self.white:
            self.board.addPiece(piece)
        self.board.fillBlanks()
        print("")

    def test_even_heuristic(self):
        self.board.printBoard()
        print("---------------------------------------")
        white = calculateHeuristic(self.board, w)
        black = calculateHeuristic(self.board, b)
        self.assertEqual(black, white)

    def test_black_advantage(self):
        self.board.movePiece((0,0), (0,2))
        self.board.printBoard()
        print("---------------------------------------")
        white = calculateHeuristic(self.board, w)
        black = calculateHeuristic(self.board, b)
        self.assertGreater(black, white)
