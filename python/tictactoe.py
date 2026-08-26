import sys

board = [
  "1", "2", "3",
  "4", "5", "6",
  "7", "8", "9"
]
players = ["X", "O"]


def print_board() -> None:
  print(f" {board[0]} ┃ {board[1]} ┃ {board[2]}")
  print("━━━╋━━━╋━━━")
  print(f" {board[3]} ┃ {board[4]} ┃ {board[5]}")
  print("━━━╋━━━╋━━━")
  print(f" {board[6]} ┃ {board[7]} ┃ {board[8]}")


def check_win():
  for player in players:
    for i in range(3):
      if (
        board[0 + i * 3] == board[1 + i * 3] == board[2 + i * 3] == player
        or board[i + 0] == board[i + 3] == board[i + 6] == player
        or board[0] == board[4] == board[8] == player
        or board[2] == board[4] == board[6] == player
      ):
        return player
  return False


def check_stale():
  for i in board:
    if i not in players:
      return False
  return True


print_board()

while True:
  for player in players:
    while True:
      try:
        chosen_pos = int(input("Wähle ein Feld  ")) - 1
        if board[chosen_pos] not in players:
          board[chosen_pos] = player
          break
      except (ValueError, IndexError):
        pass
      print("Invalid position!")
    print_board()

    winstatus = check_win()
    if winstatus:
      print(f"Player {winstatus} won!")
      sys.exit()
    elif check_stale():
      print("Stalemate!")
      sys.exit()
