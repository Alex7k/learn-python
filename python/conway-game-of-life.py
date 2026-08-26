import copy
import time

# board dimensions
WIDTH = 40
HEIGHT = 40

INTERVAL = 0.1  # time per generation (frame) in seconds

SHAPES = {
    # shape 1. default preset on a game of life website
    "shape1": """
        ...#
        .###
        ##..
        #...
    """,
    # our shape. interesting looking. made mistakenly while trying to create pulsar
    "mistake": """
        ..###...###..
        #....#.#....#
        #....#.#....#
        #....#.#....#
        ..###...###..
        .............
        ..###...###..
        #....#.#....#
        #....#.#....#
        #....#.#....#
        ..###...###..
    """,
    # Beacon, period 2
    "beacon": """
        ##..
        #...
        ...#
        ..##
    """,
    # Pulsar - Oscillator, period 3
    "pulsar": """
        ..###...###..
        .............
        #....#.#....#
        #....#.#....#
        #....#.#....#
        ..###...###..
        .............
        ..###...###..
        #....#.#....#
        #....#.#....#
        #....#.#....#
        .............
        ..###...###..
    """,
    "glider": """
        ###
        ..#
        .#.
    """,
    # Lightweight spaceship LWSS
    "lwss": """
        #..#.
        ....#
        #...#
        .####
    """,
    # middleweight spaceship
    "mwss": """
        ..#...
        #...#.
        .....#
        #....#
        .#####
    """,
    # heavyweight spaceship
    "hwss": """
        ..##...
        #....#.
        ......#
        #.....#
        .######
    """,
    # Pentadecathlon (period 15)
    "pentadecathlon": """
        ###
        .#.
        .#.
        ###
        ...
        ###
        ###
        ...
        ###
        .#.
        .#.
        ###
    """,
}

WHITE = "\033[47m  \033[0m"
BLACK = "\033[40m  \033[0m"

board = [[False] * WIDTH for _ in range(HEIGHT)]


def print_board():
    print("\033[H\033[J", end="")  # clear screen

    for row in board:
        print("".join(BLACK if cell else WHITE for cell in row))


def count_neighbors(row: int, col: int) -> int:
    count = 0
    for i in [-1, 0, 1]:
        for o in [-1, 0, 1]:
            if i == o == 0:
                continue
            if board[(row + i) % HEIGHT][(col + o) % WIDTH] == True:
                count += 1
    return count


def place(shape: str, top: int, left: int) -> None:
    for r, line in enumerate(SHAPES[shape].strip().splitlines()):
        for c, ch in enumerate(line.strip()):
            if ch == "#":
                board[(top + r) % HEIGHT][(left + c) % WIDTH] = True


place("mistake", 10, 10)


def next_state(alive: bool, neighbors: int) -> bool:
    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if alive and neighbors < 2:
        return False
    # Any live cell with two or three live neighbours lives on to the next generation.
    if alive and neighbors in [2, 3]:
        return True
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    if alive and neighbors > 3:
        return False
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    if not alive and neighbors == 3:
        return True
    return alive


while True:
    print_board()
    board_temp = copy.deepcopy(board)
    for row in range(HEIGHT):
        for col in range(WIDTH):
            board_temp[row][col] = next_state(board[row][col], count_neighbors(row, col))

    board = board_temp
    time.sleep(INTERVAL)
