import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import King, Knight

class TestKnight(unittest.TestCase):

    board = None
    wknight = None

    def setUp(self):
        self.board =  Board(5,5)
        self.wknight = Knight(self.board, (2,2), "White")
        self.board.addPiece(self.wknight)
        self.board.fillBlanks()
        print("")

    def test_get_possible_center(self):
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.wknight.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,3),(0,1),(1,0),(1,4),(3,0),(3,4),(4,1),(4,3)])
        self.assertEqual(len(moves), 8)

    def test_can_attack(self):
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.wknight.canAttack((3,0))
        self.assertEqual(result, True)
        result = self.wknight.canAttack((3,4))
        self.assertEqual(result, True)
        result = self.wknight.canAttack((0,1))
        self.assertEqual(result, True)
        result = self.wknight.canAttack((0,0))
        self.assertEqual(result, False)


    def test_get_possible_captures(self):
        self.board.addPiece(Knight(self.board, (1,4), "Black"))
        self.board.addPiece(Knight(self.board, (3,0), "Black"))
        self.board.addPiece(Knight(self.board, (3,4), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.wknight.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,3),(0,1),(1,0),(1,4),(3,0),(3,4),(4,1),(4,3)])
        self.assertEqual(len(moves), 8)

    def test_get_possible_blocked(self):
        self.board.addPiece(Knight(self.board, (1,4), "White"))
        self.board.addPiece(Knight(self.board, (3,0), "White"))
        self.board.addPiece(Knight(self.board, (3,4), "White"))
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.wknight.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,3),(0,1),(1,0),(4,1),(4,3)])
        self.assertEqual(len(moves), 5)
