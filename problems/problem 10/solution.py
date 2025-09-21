#Update this code.

def make_board(width, height):
  return [[" "]*width]*height


board = make_board(3,3)
board[0][0] = "x"
print(board)
