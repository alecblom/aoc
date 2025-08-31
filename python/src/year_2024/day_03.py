import re

EXAMPLE_INPUT_ONE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
EXAMPLE_INPUT_TWO = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def mul(a: int, b: int) -> int:
    return a*b

def part_one(input: str = EXAMPLE_INPUT_ONE):
    matches = re.findall('(mul\([0-9]{1,3},[0-9]{1,3}\))', input)
    sum = 0
    for match in matches:
        sum += eval(match)

    return sum

def part_two(input: str = EXAMPLE_INPUT_TWO):
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

def main(input: str):
    return part_one(input), part_two(input)
