import chess as c
b = c.Board()
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
while not b.is_game_over():
    print(f"\033[H\033[J{b}\n" , end = "")
    d = input("make your move: ")
    try:
        if c.Move.from_uci(d) in b.legal_moves:
                b.push(c.Move.from_uci(d))
                b.push(get(b))
    except (c.InvalidMoveError , ValueError):
        print("put your move in valid uci format, dingus")
        input("press any key to continue")
    except IndexError:
        print("you/computer won")
    except AttributeError:
        print("you/computer won")
b2 = b.outcome()
if b2:
    print(b2.termination)
    print(b2.result())
    print(b2.winner)