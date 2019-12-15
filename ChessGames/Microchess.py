from Pieces.AllPieces import *
from Board import Board

w = "White"
b = "Black"
class Microchess():

    board = None
    black = []
    white = []

    def __init__(self):
        self.board = Board(4,5)
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
        self.board.printBoard()
