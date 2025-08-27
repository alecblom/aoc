import core.helpers as helpers

_input = helpers.get_input()
_board: list[list] = []



def part_one():
    set_board()

    result = 0
    for (y, row) in enumerate(_board):
        for (x, cell) in enumerate(row):
            if cell == 'X':
                for direction in get_directions(x, y):
                    if find_xmas((x,y), direction): result += 1

    print(f"Answer: {result}")


def part_two():
    d = ""

def set_board():
    for line in _input.splitlines(): _board.append(list(line))

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

if __name__ == "__main__":
    part_one()
