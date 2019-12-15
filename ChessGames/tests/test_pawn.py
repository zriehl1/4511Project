import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import King, Pawn

class TestPawn(unittest.TestCase):

    board = None
    bpiece = None
    bking = None
    wpiece = None
    wking = None

    def setUp(self):
        self.board = Board(5,5)
        self.bking = King(self.board, (2,3), "Black")
        self.wking = King(self.board, (4,3), "White")
        self.bpiece = Pawn(self.board, (0,4), "Black")
        self.wpiece = Pawn(self.board, (0,0), "White")
        self.board.addPiece(self.bking)
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bpiece)
        self.board.addPiece(self.wpiece)
        self.board.fillBlanks()
        print("")

    def test_white_moves(self):
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.wpiece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,1),(0,2)])
        self.assertEqual(len(moves), 2)

    def test_can_attack(self):
        board = Board(5,5)
        pawn = Pawn(board, (2,0), "White")
        board.addPiece(pawn)
        board.addPiece(Pawn(board, (1,1), 'Black'))
        board.fillBlanks()
        board.printBoard()
        print("-------------------------------------------")
        result = pawn.canAttack((1,1))
        self.assertEqual(result, True)
        result = pawn.canAttack((3,1))
        self.assertEqual(result, False)
        result = pawn.canAttack((2,1))
        self.assertEqual(result, False)


    def test_black_moves(self):
        self.board.printBoard()
        print("-------------------------------------------")
        moves = self.bpiece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(0,3),(0,2)])
        self.assertEqual(len(moves), 2)

    def test_move_white(self):
        self.board.printBoard()
        print("-------------------------------------------")
        self.wpiece.moved = True
        moves = self.wpiece.getValidPositions()
        self.assertEqual(moves, [(0,1)])

    def test_captures_white(self):
        board = Board(5,5)
        piece = Pawn(board, (2,0), "White")
        board.addPiece(piece)
        board.addPiece(Pawn(board, (1,1), "Black"))
        board.addPiece(Pawn(board, (3,1), "Black"))
        board.fillBlanks()
        board.printBoard()
        print("-------------------------------------------")
        moves = piece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(2,1),(2,2),(1,1),(3,1)])
        self.assertEqual(len(moves), 4)

    def test_move_black(self):
        board = Board(5,5)
        piece = Pawn(board, (2,4), "Black")
        board.addPiece(piece)
        board.addPiece(Pawn(board, (1,3), "White"))
        board.addPiece(Pawn(board, (3,3), "White"))
        board.fillBlanks()
        board.printBoard()
        print("-------------------------------------------")
        moves = piece.getValidPositions()
        for el in moves:
            self.assertIn(el, [(2,3),(2,2),(1,3),(3,3)])
        self.assertEqual(len(moves), 4)










#
