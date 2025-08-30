from app.helpers.core import get_input
from app.day_01.main import part_one, part_two

_input = get_input(day=1, example=True)

def test_day_one() -> None:
    result = part_one(_input)
    assert result == 11
    return result

def test_day_two() -> None:
    result = part_two(_input)
    assert result == 31
    return result

def main():
    result_one = test_day_one()
    result_two = test_day_two()

    print(f"Test one: {result_one}")
    print(f"Test two: {result_two}")
