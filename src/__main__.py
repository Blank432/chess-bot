from .draw import Board
from .__init__ import POSITIONS, FILES

player = True

def draw(player):
    board = [[0 for j in range(8)] for i in range(8)]
    for piece, pos in POSITIONS.items():
        board[int(pos[1])-1][FILES.index(pos[0])] = piece
    print(board)
    board.reverse()
    board_im = Board()
    board_im.create(player, board)

def get_key(value, dict):
    return [k for k, v in dict.items() if v==value][0]

while True:
    draw(player)
    move = input()
    POSITIONS[get_key(move[:2], POSITIONS)] = move[2:]
    # player = not player