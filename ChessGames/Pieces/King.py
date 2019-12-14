class King(Piece):

    #right, left, up, down, up right, down right, up left, down left
    possible_moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    def __init__(self, board, start_x, start_y, color):
        super().__init__(board, start_x, start_y, color, "K")
