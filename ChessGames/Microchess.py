from Pieces.AllPieces import *
from Board import Board

w = "White"
b = "Black"
class Microchess():

    board = None
    black = []
    white = []
    turn = 0

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

    def move(self, start, to):
        return self.board.movePiece(start, to)

    def play(self, allowAI=False, colorAI=None):
        inv = False
        while True:
            moveFromWhite = (-1,-1)
            moveToWhite = (-1,-1)
            moveFromBlack = (-1,-1)
            moveToBlack = (-1,-1)
            while self.turn % 2 == 0:
                if self.board.isCheckmate("White"):
                    print("Game over: Black Wins!")
                    return
                if allowAI and colorAI == "White":
                    pass # get the board for the AI to calc on
                else:
                    whiteIn = input("White x y move from: ")
                    moveFromWhite = (int(whiteIn.split(" ")[0]), int(whiteIn.split(" ")[1]))
                    whiteIn2 = input("White x y move to: ")
                    moveToWhite = (int(whiteIn2.split(" ")[0]), int(whiteIn2.split(" ")[1]))
                if self.move(moveFromWhite, moveToWhite):
                    self.board.printBoard()
                    self.turn += 1
                    inv = False
                else:
                    inv = True
            while self.turn % 2 == 1:
                if self.board.isCheckmate("Black"):
                    print("Game over: White Wins!")
                    return
                if allowAI and colorAI == "Black":
                    pass # get the board for the AI to calc on
                else:
                    blackIn = input("Black x y move from: ")
                    moveFromBlack = (int(blackIn.split(" ")[0]), int(blackIn.split(" ")[1]))
                    blackIn2 = input("Black x y move to: ")
                    moveToBlack = (int(blackIn2.split(" ")[0]), int(blackIn2.split(" ")[1]))
                if self.move(moveFromBlack, moveToBlack):
                    self.board.printBoard()
                    self.turn += 1
                    inv = False
                else:
                    inv = True



if __name__ == "__main__":
    a = Microchess()
    a.play()










#
