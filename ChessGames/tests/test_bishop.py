import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import King, Bishop

class TestBishop(unittest.TestCase):

    board = None
    bpiece = None
    bking = None
    wpiece = None
    wking = None

    def setUp(self):
        self.board = Board(5,5)
        self.bking = King(self.board, (2,3), "Black")
        self.wking = King(self.board, (3,3), "White")
        self.bpiece = Bishop(self.board, (2,2), "Black")
        self.wpiece = Bishop(self.board, (1,3), "White")
        self.board.addPiece(self.bking)
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bpiece)
        self.board.addPiece(self.wpiece)
        self.board.fillBlanks()
        print("")

    def test_get_possible_blocked(self):
        self.board.addPiece(Bishop(self.board, (1,1), "Black"))
        self.board.addPiece(Bishop(self.board, (3,1), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        moves =  self.bpiece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(1,3),(3,3)])
        self.assertEqual(len(moves),2)

    def test_get_possible_unblocked(self):
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.bpiece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,0),(1,1),(3,3),(1,3),(3,1),(4,0)])
        self.assertEqual(len(moves), 6)

    def test_get_possible_center(self):
        board = Board(5,5)
        bishop = Bishop(board, (2,2), "Black")
        board.addPiece(bishop)
        board.fillBlanks()
        self.board.printBoard()
        print("-------------------------------------------")
        moves = bishop.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,0),(1,1),(3,3),(4,4),(0,4),(1,3),(3,1),(4,0)])
        self.assertEqual(len(moves), 8)

    def test_can_attack(self):
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.bpiece.canAttack((3,1))
        self.assertNotEqual(result, False)
        result = self.bpiece.canAttack((4,0))
        self.assertNotEqual(result, False)
        result = self.bpiece.canAttack((3,3))
        self.assertNotEqual(result, False)























#
