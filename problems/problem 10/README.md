Description:
Fix the following Python code so that modifying one row of the board doesn’t affect all rows.

def make_board(width, height):
  return [[" "]*width]*height

board = make_board(3,3)
board[0][0] = "x"
print(board) # should only change top-left, but changes entire column