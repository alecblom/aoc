from src.helpers.core import get_input

def part_one(input: str):
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

def part_two(input: str):
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

def main(input: str) -> tuple[int, int]:
    return part_one(input), part_two(input)

if __name__ == "__main__":
    main()