class Pawn(Piece):

    has_moved = False
    # forward, forward(unmoved), capture right, capture left
    possible_moves = [(0,1),(0,2),(1,1),(-1,1)]

    def __init__(self, board, start_x, start_y, color):
        super().__init__(self, board, start_x, start_y, color, "P")

    # returns a list of new boards for every valid move by the piece
    def getAllMoves(self):
        pass
