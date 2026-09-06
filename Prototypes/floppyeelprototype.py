import chess
import random
b = chess.Board()
while not  b.is_game_over():
    movelist = list(b.legal_moves)
    choicepick = random.choice(movelist)
    move = b.push(choicepick)
print(b)
print(b.result())