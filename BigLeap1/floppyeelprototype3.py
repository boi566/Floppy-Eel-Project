# drop your position in regular fen
import chess as c
d = input("enter a position: ")
b = c.Board(d)
VALS = {c.PAWN: 100 ,
        c.BISHOP: 300,
        c.KNIGHT: 300,
        c.ROOK : 500,
        c.QUEEN: 900,
        c.KING: 20000}
def evl(b):
    if b.is_checkmate():
        if b.turn == c.WHITE:
                return(-10000)
        elif b.turn == c.BLACK:
                return(+10000)
    elif b.is_game_over():
        return(0)
    score = 0
    for i in b.piece_map().values():
        if i.color == c.WHITE:
            score += VALS[i.piece_type]
        elif i.color == c.BLACK:
            score -= VALS[i.piece_type]
    return(score)
def get(b):
     if b.turn == c.WHITE:
            lowscore = -99999
            lowmove = None            
            for move in list(b.legal_moves):
                b.push(move)
                score = evl(b)
                b.pop()
                if lowscore < score:
                    lowscore = score
                    lowmove = move
     elif b.turn == c.BLACK:
            lowscore = 99999
            lowmove = None
            for move in list(b.legal_moves):
                b.push(move)
                score = evl(b)
                b.pop()
                if lowscore > score:
                    lowscore = score
                    lowmove = move
     return(lowmove)
print(get(b))
print(b)