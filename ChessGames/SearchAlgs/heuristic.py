char_to_val = {
    "K" : 10,
    "H" : 3,
    "B" : 3,
    "P" : 1,
    "R" : 5
}

combo_val = {
    "HR" : 6,
    "BR" : 8
}

center_tiles = [(1,2),(2,2)]

CENTER_CONTROL = 2
CHECK_PENALTY = 4
UNGUARDED_PENALTY = 4
ATTACKING_BONUS = 2


# takes a calculated value of the current position for <color> this is in no way optimized
# heuristic summary: sum of piece values minus oponnent values, combo values if applicable, self-check penalty, checkmate reward, capture opportunity penalty, attack capture bonus
# probaby a pretty poor heuristic
def calculateHeuristic(board, color):
    heuristicVal = 0
    defenders = None
    attackers = None
    aColor = None
    if color == "White":
        defenders = board.white
        attackers = board.black
        aColor = "Black"
    else:
        defenders = board.black
        attackers = board.white
        aColor = "White"
    hasKnight = False
    hasRook = False
    hasBishop = False
    for piece in defenders:
        heuristicVal += char_to_val[piece.getChar()]
        if piece.getChar() == "H":
            hasKnight = True
        elif piece.getChar() == "R":
            hasRook = True
        elif piece.getChar() == "B":
            hasBishop = True
    if hasRook and hasBishop:
        #print("Bishop Rook bonus")
        heuristicVal += combo_val["BR"]
    if hasRook and hasKnight:
        #print("Rook Knight bonus")
        heuristicVal += combo_val["HR"]
    for piece in attackers:
        heuristicVal -= char_to_val[piece.getChar()]
    for piece in defenders:
        for tile in center_tiles:
            if piece.canAttack(tile):
                #print("Center control")
                heuristicVal += CENTER_CONTROL
    if board.checkKing(color):
        heuristicVal -= CHECK_PENALTY
    if board.isCheckmate(color):
        heuristicVal -= 100
    elif board.isCheckmate(aColor):
        heuristicVal += 100
    defenderPositions = []
    for piece in defenders:
        defenderPositions.append(piece.getPos())
    for pos in defenderPositions:
        if board.isGuarded(pos, color):
            continue
        elif board.isGuarded(pos, aColor):
            #print("Unguarded Penalty")
            heuristicVal -= UNGUARDED_PENALTY
    attackerPositions = []
    for piece in attackers:
        attackerPositions.append(piece.getPos())
    for pos in attackerPositions:
        if board.isGuarded(pos, aColor):
            continue
        elif board.isGuarded(pos, color):
            #print("Attack Bonus")
            heuristicVal += ATTACKING_BONUS
    return heuristicVal














#
