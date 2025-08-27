import core.helpers as helpers
import re

def part_one():
    input = helpers.get_input()
    matches = re.findall('(mul\([0-9]{1,3},[0-9]{1,3}\))', input)
    sum = 0
    for match in matches:
        sum += eval(match)
    
    print(f"Answer: {sum}")

def part_two():
    input = helpers.get_input()
    matches = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))", input)
    enabled = True
    sum = 0
    for cmd in matches:
        match cmd:
            case 'do()': enabled = True
            case 'don\'t()': enabled = False
            case _:
                if enabled: sum += eval(cmd)
    print(f"Answer: {sum}")

def mul(a: int, b: int) -> int:
    return a*b

if __name__ == "__main__":
    part_one()
    part_two()