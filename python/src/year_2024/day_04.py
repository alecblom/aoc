EXAMPLE_INPUT_ONE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

EXAMPLE_INPUT_TWO = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

_board: list[list] = []

def set_board(input: str):
    for line in input.splitlines(): _board.append(list(line))

def get_directions(x: int, y: int) -> list[str]:
    directions = []
    right, left = False, False
    if(x <= (len(_board[y]) - 4)):
        directions.append("right")
        right = True
    if(x >= 3):
        directions.append("left")
        left = True
    if(y <= (len(_board) - 4)):
        directions.append("down")
        if right: directions.append("down-right")
        if left: directions.append("down-left")
    if(y >= 3):
        directions.append("up")
        if right: directions.append("up-right")
        if left: directions.append("up-left")
    return directions

def find_xmas(start_pos: tuple[int, int], direction: str) -> bool:
    for (i, letter) in enumerate(list("XMAS")):
        current = step(start_pos, direction, i)
        if current is not letter: return False

    return True

def step(start_pos: tuple[int, int], direction: str, step_size: int = 1):
    x, y = start_pos[0], start_pos[1]
    if "right" in direction:
        x += step_size
    if "left" in direction:
        x -= step_size
    if "up" in direction:
        y -= step_size
    if "down" in direction:
        y += step_size

    return _board[y][x]

def part_one(input: str = EXAMPLE_INPUT_ONE):
    set_board(input)

    result = 0
    for (y, row) in enumerate(_board):
        for (x, cell) in enumerate(row):
            if cell == 'X':
                for direction in get_directions(x, y):
                    if find_xmas((x,y), direction): result += 1

    return result


def part_two(input: str = EXAMPLE_INPUT_TWO):
    raise NotImplementedError("Day 4 part two not implemented yet")


def main(input: str):
    return part_one(input), part_two(input)
