import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))
from Board import Board

from Pieces.AllPieces import *

class TestBoard(unittest.TestCase):

    board = None
    wking = None
    bking = None
    bpawn = None
    brook = None
    wrook = None

    def setUp(self):
        self.board = Board(5,5)
        self.wking = King(self.board, (4,4), "White")
        self.bking = King(self.board, (1,0), "Black")
        self.bpawn = Pawn(self.board, (0,1), "Black")
        self.brook = Rook(self.board, (4,0), "Black")
        self.wrook = Rook(self.board, (4,3), "White")
        self.board.fillBlanks()
        print("")

    def test_place_pieces(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(self.wrook)
        self.board.printBoard()
        print("-------------------------------------------")

    def test_check_king(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(Bishop(self.board, (4,3), "White"))
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.board.checkKing("Black")
        self.assertEqual(result, True)

    # attempting to move a piece that isnt the king while in check should be blocked
    def test_move_in_check_error(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(self.wrook)
        result = self.board.movePiece((0,1),(0,2))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(result, False)

    def test_move_in_check_success(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(self.wrook)
        result = self.board.movePiece((1,0),(1,1))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(result, True)

    def test_move_pinned_error(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(self.wrook)
        result = self.board.movePiece((4,3),(3,3))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(result, False)

    def test_move_pinned_success(self):
        self.board.addPiece(self.wking)
        self.board.addPiece(self.bking)
        self.board.addPiece(self.bpawn)
        self.board.addPiece(self.brook)
        self.board.addPiece(self.wrook)
        result = self.board.movePiece((4,3),(4,2))
        self.board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(result, True)

    def test_king_quirk(self):
        board = Board(5,5)
        board.addPiece(King(board, (2,2), "Black"))
        board.addPiece(King(board, (0,2), "White"))
        board.fillBlanks()
        result = board.movePiece((0,2),(1,2))
        board.printBoard()
        print("-------------------------------------------")
        self.assertEqual(result, False)

    def test_checkmate_distance(self):
        self.board.addPiece(King(self.board, (0,4), "Black"))
        self.board.addPiece(Rook(self.board, (0,2), "White"))
        self.board.addPiece(Rook(self.board, (2,4), "White"))
        self.board.addPiece(King(self.board, (2,2), "White"))
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.board.isCheckmate("Black")
        self.assertEqual(result, True)

    def test_checkmate_uncaptureable(self):
        self.board.addPiece(King(self.board, (0,4), "Black"))
        self.board.addPiece(Rook(self.board, (0,2), "White"))
        self.board.addPiece(Rook(self.board, (2,4), "White"))
        self.board.addPiece(Rook(self.board, (0,3), "White"))
        self.board.addPiece(King(self.board, (2,2), "White"))
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.board.isCheckmate("Black")
        self.assertEqual(result, True)

    def test_not_checkmate1(self):
        self.board.addPiece(King(self.board, (2,0), "White"))
        self.board.addPiece(Rook(self.board, (1,0), "Black"))
        self.board.addPiece(Rook(self.board, (4,1), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.board.isCheckmate("White")
        self.assertEqual(result, False)

    def test_not_checkmate2(self):
        self.board.addPiece(King(self.board, (2,0), "White"))
        self.board.addPiece(Rook(self.board, (1,1), "White"))
        self.board.addPiece(Rook(self.board, (0,0), "Black"))
        self.board.addPiece(Rook(self.board, (4,1), "Black"))
        self.board.printBoard()
        print("-------------------------------------------")
        result = self.board.isCheckmate("White")
        self.assertEqual(result, False)

    def test_not_checkmate3(self):
        self.board.addPiece(King(self.board, (2,0), "White"))
        self.board.addPiece(Rook(self.board, (3,4), "Black"))
        self.board.addPiece(Rook(self.board, (1,4), "Black"))
        self.board.addPiece(Rook(self.board, (0,1), "Black"))
        self.board.addPiece(Knight(self.board, (4,1), "Black"))
        self.board.addPiece(Rook(self.board, (4,2), "White"))
        self.board.printBoard()
        print("-------------------------------------------")
        check = self.board.checkKing("White")
        self.assertEqual(check, True)
        checkmate = self.board.isCheckmate("White")
        self.assertEqual(checkmate, False)



#
