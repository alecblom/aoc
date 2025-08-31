EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""

def part_one(input: str = EXAMPLE_INPUT):
    answer = 0
    list_one, list_two = [], []
    for line in iter(input.splitlines()):
        lst = line.split()
        first, last = int(lst[0]), int(lst[-1])
        list_one.append(first)
        list_two.append(last)

    list_one.sort()
    list_two.sort()

    for one, two in zip(list_one, list_two):
        answer += abs(one-two)

    return answer

def part_two(input: str = EXAMPLE_INPUT):
    answer = 0
    list_one, list_two = [], []

    for line in iter(input.splitlines()):
        lst = line.split()
        first, last = int(lst[0]), int(lst[-1])
        list_one.append(first)
        list_two.append(last)

    for item in list_one:
        answer += item * list_two.count(item)

    return answer

def main(input: str):
    return part_one(input), part_two(input)
