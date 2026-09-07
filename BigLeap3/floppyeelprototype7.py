# play with the alpha beta pruned version
import chess as c
b = c.Board()
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
def get(b , depth,
alpha = float('-inf'),
beta = float('inf')):
    if depth == 0 or b.is_game_over():
        return(evl(b , depth) , None)
    if b.turn == c.WHITE:
        maximum = float('-inf')
        lowmove = None            
        for move in b.legal_moves:
            b.push(move)
            score , _ = get(b , depth - 1 , alpha , beta)
            b.pop()
            if score > maximum:
                maximum = score
                lowmove = move
                alpha = max(alpha , score)
                if beta <= alpha:
                    break
        return(maximum , lowmove)
    elif b.turn == c.BLACK:
        minimum = float('inf')
        lowmove = None
        for move in b.legal_moves:
            b.push(move)
            score , _ = get(b , depth - 1 , alpha , beta)
            b.pop()
            if score < minimum:
                minimum = score
                lowmove = move
                beta = min(beta , score)
                if beta <= alpha:
                    break
        return(minimum , lowmove)
depth = 3
while not b.is_game_over():
    print(f"\033[H\033[J{b}\n" , end = "")
    d = input("make your move: ")
    try:
        if c.Move.from_uci(d) in b.legal_moves:
                b.push(c.Move.from_uci(d))
                l = list(b.legal_moves)
                s , z = get(b , depth)
                b.push(z)
    except (c.InvalidMoveError , ValueError):
        print("put your move in valid uci format, dingus")
        input("press enter to exit")
    except IndexError:
        print("you/computer won")
b2 = board.outcome()
if b2:
    print(b2.termination)
    print(b2.result())
    print(b2.winner)