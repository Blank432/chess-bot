from init import Board
pieces = ['bb1', 'bb2', 'bk', 'bn1', 'bn2', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8', 'bq', 'br1', 'br2', 'wb1', 'wb2', 'wk', 'wn1', 'wn2', 'wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8', 'wq', 'wr1', 'wr2']
initial_board = [
    ['br1', 'bb1', 'bn1', 'bq', 'bk2', 'bn2', 'bb2', 'br2'],
    ['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['wr1', 'wb1', 'wn1', 'wq', 'wk2', 'wn2', 'wb2', 'wr2'],
    ['wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8'],
]

board = Board()
board.board(True, initial_board)