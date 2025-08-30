import re

def mul(a: int, b: int) -> int:
    return a*b

def part_one(input: str):
    matches = re.findall('(mul\([0-9]{1,3},[0-9]{1,3}\))', input)
    sum = 0
    for match in matches:
        sum += eval(match)

    return sum

def part_two(input: str):
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

if __name__ == "__main__":
    main()