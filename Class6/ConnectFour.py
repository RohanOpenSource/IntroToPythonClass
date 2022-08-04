#initialize board
board = []
rows = 5
cols = 7

def init_board():
  for i in range(0, rows):
    row = []
    for j in range(0, cols):
      row.append(" ")
    board.append(row)
init_board()

#print board

def print_board():
  #first line
  row = ""
  for i in range(0, cols):
    row += " " + str(i)
  print(row)
  #Start with board
  for i in board:
    row = "|"
    for j in i:
      row += str(j) +"|"
    print(row)
    print("+" + "-+" * cols)
  
print_board()

# 0 1 2 3 4
#| | | | | |
#+-+-+-+-+-+
#| |2| | | |
#+-+-+-+-+-+
#| |1| | | |
#+-+-+-+-+-+
#| |1|2| | |
#+-+-+-+-+-+

#player turn
def player_turn(player, col):
  works = False
  if(not (col >= 0 and col < cols)):
    return False
  
  for i in range(rows-1, -1, -1):
    if(board[i][col] == " "):
      works = True
      board[i][col] = str(player)
      break
  return works

#check for wins
def get_game_state():
  one_i = 0 #curr number of consectuive 1s
  two_i = 0
  one_max = 0 #max number of consecutive 1s
  two_max = 0
  for i in range(rows):
    for j in range(cols):
      if(board[i][j] == "1"):
        one_i+= 1
      else:
        one_max = max(one_max, one_i)
        one_i = 0
      if(board[i][j] == "2"):
        two_i += 1
      else:
        two_max = max(two_max, two_i)
        two_i = 0
    one_max = max(one_max, one_i)
    two_max = max(two_max, two_i)
    one_i = 0
    two_i = 0
  for i in range(cols):
    for j in range(rows):
      if(board[j][i] == "1"):
        one_i+= 1
      else:
        one_max = max(one_max, one_i)
        one_i = 0
      if(board[j][i] == "2"):
        two_i += 1
      else:
        two_max = max(two_max, two_i)
        two_i = 0
    one_max = max(one_max, one_i)
    two_max = max(two_max, two_i)
    one_i = 0
    two_i = 0
  for i in range(3, rows):
    for j in range(cols - 3):
      if(board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] != " "):
        return int(board[i][j])
  for i in range(3, rows):
    for j in range(3, cols):
      if(board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i-3][j-3] != " "):
        return int(board[i][j])
  
  if(one_max >= 4): 
    return 1
  if(two_max >= 4): 
    return 2
  return 0

#actual game
turn = 0
while(True):
  player = turn % 2 + 1
  print("Player " + str(player))
  works = False
  while(not works):
    move = int(input("which column do you want to play in? "))
    works =  player_turn(player, move)
  game_state = get_game_state()
  print_board()
  if(game_state != 0):
    break
  turn += 1

#print who won
print("Player " + str(get_game_state()) +" won! Good job!")
