import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import King, Rook

class TestKing(unittest.TestCase):

    board = None
    wking = None

    def setUp(self):
        self.board = Board(5,5)
        self.wking = King(self.board, (2,2), "White")
        self.board.addPiece(self.wking)
        self.board.fillBlanks()
        print("")

    def test_empty_board(self):
        board = Board(5,5)
        king = King(board, (2,2), "White")
        board.addPiece(king)
        board.fillBlanks()
        board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(board.black), 0)
        moves = king.getValidPositions()
        self.assertEqual(len(moves), 8)

    def test_can_attack(self):
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.wking.canAttack((3,3))
        self.assertNotEqual(result, False)
        result = self.wking.canAttack((3,1))
        self.assertNotEqual(result, False)
        result = self.wking.canAttack((1,1))
        self.assertNotEqual(result, False)
        result = self.wking.canAttack((0,0))
        self.assertEqual(result, False)

    def test_block_top(self):
        self.board.addPiece(Rook(self.board, (4,3), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(self.board.black), 1)
        moves = self.wking.getValidPositions()
        for el in moves:
            self.assertNotIn(el, [(1,3),(2,3),(3,3)])
        self.assertEqual(len(moves), 5)

    def test_block_left(self):
        self.board.addPiece(Rook(self.board, (1,4), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(self.board.black), 1)
        moves = self.wking.getValidPositions()
        for el in moves:
            self.assertNotIn(el, [(1,3),(1,2),(1,1)])
        self.assertEqual(len(moves), 5)

    def test_block_all(self):
        self.board.addPiece(Rook(self.board, (1,4), "Black"))
        self.board.addPiece(Rook(self.board, (4,3), "Black"))
        self.board.addPiece(Rook(self.board, (0,1), "Black"))
        self.board.addPiece(Rook(self.board, (3,0), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(self.board.black), 4)
        moves = self.wking.getValidPositions()
        self.assertEqual(len(moves), 0)

    def test_capture_check(self):
        self.board.addPiece(Rook(self.board, (1,2), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(self.board.black), 1)
        moves = self.wking.getValidPositions()
        self.assertEqual(len(moves), 5)

    def test_guarded_capture(self):
        self.board.addPiece(Rook(self.board, (0,2), "Black"))
        self.board.addPiece(Rook(self.board, (1,2), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(len(self.board.black), 2)
        moves = self.wking.getValidPositions()
        self.assertEqual(len(moves), 4)
