EXAMPLE_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def is_valid_list(values: list[int]):
    return (sorted(values) == values or sorted(values, reverse=True) == values) and all(
        1 <= abs(values[i] - values[i+1]) <= 3 for i in range(len(values) - 1))

def part_one(input: str = EXAMPLE_INPUT):
    result = 0
    for line in input.splitlines():
        vals = list(map(int, line.split()))
        if is_valid_list(vals): result += 1
    
    return result

def part_two(input: str = EXAMPLE_INPUT):
    result = 0
    for line in input.splitlines():
        vals = list(map(int, line.split()))
        if is_valid_list(vals): result += 1
        else:
            for i in range(len(vals)):
                new_vals = vals.copy()
                del new_vals[i]
                if is_valid_list(new_vals):
                    result += 1
                    break
    return result


def main(input: str):
    return part_one(input), part_two(input)
