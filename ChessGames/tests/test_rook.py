import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import King, Rook

class TestRook(unittest.TestCase):

    board = None
    brook = None
    bking = None
    wking = None
    wrook = None

    def setUp(self):
        self.board = Board(5,5)
        self.brook = Rook(self.board, (0,0), "Black")
        self.bking = King(self.board, (4,4), "Black")
        self.wking = King(self.board, (1,1), "White")
        self.wrook = Rook(self.board, (0,1), "White")
        self.board.addPiece(self.brook)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.wking)
        self.board.addPiece(self.wrook)
        self.board.fillBlanks()
        print("")

    def test_get_possible_blocked(self):
        self.board.addPiece(Rook(self.board, (1,0), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.brook.getValidPositions()
        self.assertEqual(moves, [(0,1)])

    def test_can_attack(self):
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.brook.canAttack((0,1))
        self.assertNotEqual(result, False)
        result = self.brook.canAttack((4,0))
        self.assertNotEqual(result, False)
        result = self.brook.canAttack((1,1))
        self.assertEqual(result, False)

    def test_get_possible_unblocked(self):
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.brook.getValidPositions()
        self.assertEqual(moves, [(0,1),(1,0),(2,0),(3,0),(4,0)])

    def test_get_possible_center(self):
        board = Board(5,5)
        rook = Rook(board, (2,2), "Black")
        board.addPiece(rook)
        board.fillBlanks()
        board.printBoard()
        print("-------------------------------------------")
        moves = rook.getValidPositions()
        for move in moves:
            self.assertIn(move,[(0,2),(1,2),(3,2),(4,2),(2,0),(2,1),(2,3),(2,4)])
        self.assertEqual(len(moves), 8)
