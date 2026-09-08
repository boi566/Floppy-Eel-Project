# play with the quienstence (dont know how to spell) , delta pruned update
import chess as c
DELLA = 900
b = c.Board()
VALS = {c.PAWN: 100 ,
        c.BISHOP: 300,
        c.KNIGHT: 300,
        c.ROOK : 500,
        c.QUEEN: 900,
        c.KING: 0}
PAWN_MG = [0, 0, 0, 0, 0, 0, 0, 0, 98, 134, 61, 95, 68, 126, 34, -11, -6, 7, 26, 31, 65, 56, 25, -20, -14, 13, 6, 21, 23, 12, 17, -23, -27, -2, -5, 12, 17, 6, 10, -25, -26, -4, -4, -10, 3, 3, 33, -12, -35, -1, -20, -23, -15, 24, 38, -22, 0, 0, 0, 0, 0, 0, 0, 0]
KNIGHT_MG = [-167, -89, -34, -49, 61, -97, -15, -107, -73, -41, 72, 36, 23, 62, 7, -17, -47, 60, 37, 65, 84, 129, 73, 44, -9, 17, 19, 53, 37, 69, 18, 22, -13, 4, 16, 13, 28, 19, 21, -8, -23, -9, 12, 10, 19, 17, 25, -16, -29, -53, -12, 3, -1, 18, -14, -19, -105, -21, -5, -8, -11, -23, -19, -39]
BISHOP_MG = [-29, 4, -10, -23, 5, 19, -20, -18, -25, 18, -27, 15, -5, 3, -27, -18, -10, 15, 10, 15, 16, 15, 15, -2, 7, 15, 16, 13, 14, 12, 17, -2, 8, 12, 12, 14, 11, 10, 8, 2, 8, 11, 11, 10, 11, 7, 10, 3, -1, 20, 8, -8, -11, -6, 12, -7, -33, -3, -22, -21, -13, -12, -39, -21]
ROOK_MG = [32, 42, 32, 51, 63, 9, 31, 43, 27, 32, 58, 62, 80, 67, 26, 44, -5, 19, 26, 36, 17, 45, 61, 16, -24, -11, 7, 26, 24, 35, -8, -20, -36, -26, -12, -1, 9, -7, 6, -23, -45, -25, -16, -17, 3, 0, -5, -33, -44, -16, -20, -9, -1, 11, -6, -71, -19, -13, 1, 17, 16, 7, -37, -26]
QUEEN_MG = [-28, 0, 29, 12, 59, 44, 43, 45, -24, -39, -5, 1, -16, 57, 28, 54, -13, -17, 7, 8, 29, 56, 47, 57, -27, -27, -16, -16, -1, 17, -2, 1, -9, -26, -9, -10, -2, -4, 3, -3, -14, 2, -11, -2, -5, -12, -16, -12, -35, -8, 11, 2, 8, 15, -3, 1, -1, -18, -9, 10, -15, -25, -31, -50]
KING_MG = [-65, 23, 16, -15, -56, -34, 2, 13, 29, -1, -20, -7, -8, -4, -38, -29, -9, 24, 2, -16, -20, 6, 22, -22, -17, -20, -12, -27, -30, -25, -14, -36, -49, -1, -27, -39, -46, -44, -33, -51, -14, -14, -22, -46, -44, -30, -15, -27, 1, 7, -8, -64, -43, -16, 9, 8, -15, 36, 12, -54, 8, -28, 24, 14]
THEM_TABLES = {c.PAWN : PAWN_MG,
               c.BISHOP : BISHOP_MG,
               c.KNIGHT : KNIGHT_MG,
               c.ROOK : ROOK_MG,
               c.QUEEN : QUEEN_MG,
               c.KING : KING_MG}
def evl(b , depth):
    if b.is_checkmate():
        if b.turn == c.WHITE:
                return(-1000000 - depth)
        elif b.turn == c.BLACK:
                return(+1000000 + depth)
    elif b.is_game_over():
        return(0)
    score = 0
    for sq, i in b.piece_map().items():
        if i.color == c.WHITE:
            score += VALS[i.piece_type] + THEM_TABLES[i.piece_type][sq ^ 56]
        elif i.color == c.BLACK:
            score -= VALS[i.piece_type] + THEM_TABLES[i.piece_type][sq]
    return(score)
def quench(b , alpha , beta):
    pat = evl(b , 0)
    if b.turn == c.WHITE:
       if pat >= beta:
           return(beta)
       alpha = max(alpha , pat)
       for move in b.generate_legal_captures():
           tget = b.piece_at(move.to_square)
           if tget:
               vl = VALS[tget.piece_type]
               if pat + vl + DELLA <= alpha:
                   continue
           b.push(move)
           score = quench(b , alpha , beta)
           b.pop()
           if score >= beta:
               return(beta)
           alpha = max(score , alpha)
       return(alpha)
    else:
        if pat <= alpha:
            return(alpha)
        beta = min(beta , pat)
        for move in b.generate_legal_captures():
            tget = b.piece_at(move.to_square)
            if tget:
                vl = VALS[tget.piece_type]
                if pat - vl + DELLA >= beta:
                    continue
            b.push(move)
            score = quench(b , alpha , beta)
            b.pop()
            if score <= alpha:
                return(alpha)
            beta = min(score , beta)
        return(beta)
def get(b , depth,
alpha = float('-inf'),
beta = float('inf')):
    if b.is_game_over():
        return(evl(b , depth) , None)
    if depth == 0:
        return(quench(b , alpha , beta) , None)
    leg = sorted(b.legal_moves , key = lambda m: b.is_capture(m) , reverse = True)
    if b.turn == c.WHITE:
        maximum = float('-inf')
        lowmove = None            
        for move in leg:
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
        for move in leg:
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
while not b.is_game_over():
    print(f"\033[H\033[J{b}\n" , end = "")
    d = input("make your move: ")
    try:
        if c.Move.from_uci(d) in b.legal_moves:
                b.push(c.Move.from_uci(d))
                s , z = get(b , 3)
                b.push(z)
    except (c.InvalidMoveError , ValueError):
        print("put your move in valid uci format, dingus")
    except IndexError:
        print("you/computer won")
b = board.outcome()
if b:
    print(b.termination)
    print(b.result())
    print(b.winner)