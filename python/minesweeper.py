# Console Minesweeper with board size and bomb rate adjustment support

import random
import sys

### VARIABLES
ROWS = 2
COLS = 2
BOMB_DENSITY = 0.1
bombs = int(ROWS * COLS * BOMB_DENSITY)
# bombs = int(math.sqrt(ROWS*COLS))
################

field = [["-" for x in range(COLS)] for y in range(ROWS)]
bombmap = [["-" for x in range(COLS)] for y in range(ROWS)]


def fill_bombs():
  while sum(row.count("*") for row in bombmap) < bombs:
    bombmap[random.randint(0, ROWS - 1)][random.randint(0, COLS - 1)] = "*"


fill_bombs()


def get_spaces(max, text):
  text = str(text)
  spaces_amount = max - len(text)
  spaces = ""
  for i in range(spaces_amount):
    spaces += " "
  return spaces


def print_field(show_bombs=False):
  if show_bombs:
    # Deep copy of field
    field_display = [row[:] for row in field]
    for row in range(ROWS):
      for col in range(COLS):
        if bombmap[row][col] == "*":
          field_display[row][col] = "*"
  else:
    field_display = field

  max_digits_row = 0
  for row in range(ROWS):
    length = len(str(row))
    max_digits_row = max(max_digits_row, length)
  max_digits_col = 0
  for col in range(COLS):
    length = len(str(col))
    max_digits_col = max(max_digits_col, length)

  top_legend = get_spaces(max_digits_row + 2, "")
  for col in range(COLS):  # add numbers top legend
    top_legend += str(col + 1) + get_spaces(max_digits_col + 1, col + 1)
  print(top_legend)

  for row in range(ROWS):
    indent = get_spaces(max_digits_row + 2, row + 1)
    # print(indentAmount)
    readable_row = str(row + 1) + indent
    for col in range(COLS):
      readable_row += field_display[row][col] + get_spaces(max_digits_col, "")
    print(readable_row)


def get_surrounding(row, col):
  surrounding = []
  for row_offset in (-1, 0, 1):
    for col_offset in (-1, 0, 1):
      if row_offset == col_offset == 0:
        continue  # don't count itself
      new_row = row + row_offset
      new_col = col + col_offset
      if 0 <= new_row < ROWS and 0 <= new_col < COLS:
        surrounding.append((new_row, new_col))
  return surrounding


def count_surrounding_bombs(row, col):
  count = sum(1 for r, c in get_surrounding(row, col) if bombmap[r][c] == "*")
  return str(count) if count else " "


def flag(row, col):
  if field[row][col] == "-":
    field[row][col] = "F"
  elif field[row][col] == "F":
    field[row][col] = "-"


def uncover(row, col):
  # Iterative flood fill to avoid recursion limit
  stack = [(row, col)]
  while stack:
    r, c = stack.pop()
    if field[r][c] != "-":
      continue
    if bombmap[r][c] == "*":
      return True  # BOMB UNCOVERED
    surrounding_bombs = count_surrounding_bombs(r, c)
    field[r][c] = surrounding_bombs
    if surrounding_bombs == " ":
      for nr, nc in get_surrounding(r, c):
        if field[nr][nc] == "-":
          stack.append((nr, nc))
  return False


def check_win():
  for row in range(ROWS):
    for col in range(COLS):
      # breakpoint()
      if str(bombmap[row][col]) == "-" and str(field[row][col]) != " ":
        return False
  return True


print_field(False)

while True:
  while True:
    try:
      chosen_col = int(input("Choose a column:")) - 1
      chosen_row = int(input("Choose a row:")) - 1
      if field[chosen_row][chosen_col] in ["-", "F"]:
        break
      else:
        raise
    except ValueError:
      print("Choose a different position!")
      continue
  while True:
    action = input("Choose an action -> Hit: 'x', Flag: 'f'").lower()
    if action in ["x", "f"]:
      break
    else:
      continue
  if action == "f":
    flag(chosen_row, chosen_col)
    print_field(False)
  if action == "x":
    if uncover(chosen_row, chosen_col):
      print_field(True)
      print("BOOM. You died!")
      sys.exit()
    else:
      print_field(False)
      print("Phew. No bomb.")
  if check_win():
    print(
      f"You win! Configuration: {ROWS} x {COLS} with a bomb density of {BOMB_DENSITY} ({bombs} bombs)."
    )
    sys.exit()
