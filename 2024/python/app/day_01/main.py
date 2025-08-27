from ..helpers import core

_input = core.get_input(day=1)

def part_one(input: str = _input):
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

def part_two(input: str = _input):
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

def main():
    result_one, result_two = part_one(), part_two()
    print(f"Answer one: {result_one}")
    print(f"Answer two: {result_two}")

if __name__ == "__main__":
    main()