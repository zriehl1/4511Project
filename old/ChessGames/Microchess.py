from Board import Board
from Pieces.AllPieces import *
class Microchess:\

    board = None
    black = []
    white = []
    def __init__(self):
        self.board = Board(4, 5)
        self.board.add_piece(Rook(self.board,0,0,"White"))
        self.board.add_piece(Bishop(self.board,1,0,"White"))
        self.board.add_piece(Knight(self.board,2,0,"White"))
        self.board.add_piece(King(self.board,3,0,"White"))
        self.board.add_piece(Pawn(self.board,3,1,"White"))
        self.board.add_piece(Pawn(self.board,0,3,"Black"))
        self.board.add_piece(King(self.board,0,4,"Black"))
        self.board.add_piece(Knight(self.board,1,4,"Black"))
        self.board.add_piece(Bishop(self.board,2,4,"Black"))
        self.board.add_piece(Rook(self.board,3,4,"Black"))
        self.board.fill_blanks()
        self.board.print_board()
        
