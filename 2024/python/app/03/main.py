import re
from app.helpers.core import get_input

_input = get_input(day=3)

def mul(a: int, b: int) -> int:
    return a*b

def part_one():
    matches = re.findall('(mul\([0-9]{1,3},[0-9]{1,3}\))', input)
    sum = 0
    for match in matches:
        sum += eval(match)

    return sum

def part_two():
    input = get_input()
    matches = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))", input)
    enabled = True
    sum = 0
    for cmd in matches:
        match cmd:
            case 'do()': enabled = True
            case 'don\'t()': enabled = False
            case _:
                if enabled: sum += eval(cmd)

    return sum

def main(input: str = _input):
    result_one, result_two = part_one(input), part_two(input)

    print(f"Answer one: {result_one}")
    print(f"Answer two: {result_two}")

if __name__ == "__main__":
    main()