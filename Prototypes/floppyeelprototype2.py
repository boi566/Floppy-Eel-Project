# i advise you to not play as black as it wont work
import chess
import random
board = chess.Board()
while not board.is_game_over():
    print(board)
    d = input("make your move: ")
    try:
        if chess.Move.from_uci(d) in board.legal_moves:
                board.push(chess.Move.from_uci(d))
                l = list(board.legal_moves)
                s = random.choice(l)
                board.push(s)
    except (chess.InvalidMoveError , ValueError):
        print("put your move in valid uci format, dingus")
print(board)