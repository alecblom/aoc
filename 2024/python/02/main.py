

def part_one():
    input = get_input()
    safe_reports = 0
    for line in input.splitlines():
        vals = list(map(int, line.split()))
        if is_valid_list(vals): safe_reports += 1
    
    print(safe_reports)

def part_two():
    input = get_input()
    safe_reports = 0
    for line in input.splitlines():
        vals = list(map(int, line.split()))
        if is_valid_list(vals): safe_reports += 1
        else:
            for i in range(len(vals)):
                new_vals = vals.copy()
                del new_vals[i]
                if is_valid_list(new_vals):
                    safe_reports += 1
                    break
    print(f"Answer: {safe_reports}")

def is_valid_list(values: list[int]):
    return (sorted(values) == values or sorted(values, reverse=True) == values) and all(
        1 <= abs(values[i] - values[i+1]) <= 3
        for i in range(len(values) - 1))


def get_input(file_name: str = "input.txt") -> str:
    file = open(file_name)
    content = file.read()
    file.close()
    return content

if __name__ == "__main__":
    # part_one()
    part_two()