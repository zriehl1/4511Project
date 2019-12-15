try:
    from Piece import Piece
except:
    from .Piece import Piece

class Pawn(Piece):

    def __init__(self, board, pos, color):
        super().__init__(board, pos, color, "P")
        self.direction = None
        self.buildMoveSet()

    #populate moves with all possible x,y additions
    def buildMoveSet(self):
        self.moves = []
        if self.color == "Black": # moving down
            self.direction = -1
        else: # white and moving up
            self.direction = 1

    def canAttack(self, pos):
        if pos[0] == self.pos[0]:
            return False
        return super().canAttack(pos)

    def getValidPositions(self):
        valid = []
        # check capture left
        cap_left = (self.pos[0] - 1, self.pos[1] + self.direction)
        at_left = self.board.isOccupied(cap_left)
        if at_left != None and at_left.getColor() != self.getColor() and at_left.getChar() != " ":
            valid.append(cap_left)
            #self.moved = True
        # check capture right
        cap_right = (self.pos[0] + 1, self.pos[1] + self.direction)
        at_right = self.board.isOccupied(cap_right)
        if at_right != None and at_right.getColor() != self.getColor() and at_right.getChar() != " ":
            valid.append(cap_right)
            #self.moved = True
        open_first = False
        # move one forward
        move_one = self.board.isOccupied((self.pos[0],self.pos[1]+self.direction))
        if move_one != None and move_one.getChar() == " ":
            valid.append((self.pos[0], self.pos[1]+self.direction))
            #self.moved = True
            open_first = True
        if open_first and not self.moved:
            move_two = self.board.isOccupied((self.pos[0], self.pos[1] + (2*self.direction)))
            if move_two != None and move_two.getChar() == " ":
                valid.append((self.pos[0], self.pos[1] + (2*self.direction)))
                #self.moved = True

        return valid
