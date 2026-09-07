# drop your position in regular fen
import chess as c
d = input("enter a position: ")
b = c.Board(d)
VALS = {c.PAWN: 100 ,
        c.BISHOP: 300,
        c.KNIGHT: 300,
        c.ROOK : 500,
        c.QUEEN: 900,
        c.KING: 0}
def evl(b , depth):
    if b.is_checkmate():
        if b.turn == c.WHITE:
                return(-1000000 - depth)
        elif b.turn == c.BLACK:
                return(+1000000 + depth)
    elif b.is_game_over():
        return(0)
    score = 0
    for i in b.piece_map().values():
        if i.color == c.WHITE:
            score += VALS[i.piece_type]
        elif i.color == c.BLACK:
            score -= VALS[i.piece_type]
    return(score)
def get(b , depth):
    if depth == 0 or b.is_game_over():
        return(evl(b , depth) , None)
    if b.turn == c.WHITE:
        maximum = float('-inf')
        lowmove = None            
        for move in b.legal_moves:
            b.push(move)
            score , _ = get(b , depth - 1)
            b.pop()
            if score > maximum:
                maximum = score
                lowmove = move
        return(maximum , lowmove)
    elif b.turn == c.BLACK:
        minimum = float('inf')
        lowmove = None
        for move in b.legal_moves:
            b.push(move)
            score , _ = get(b , depth - 1)
            b.pop()
            if score < minimum:
                minimum = score
                lowmove = move
        return(minimum , lowmove)
print(get(b , 3))
print(b)