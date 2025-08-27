from ..helpers import core
from main import part_one, part_two

_input = core.get_input(day=1, example=True)

def run_tests():
    test_day_one()
    test_day_two()

def test_day_one() -> None:
    assert part_one(_input) == 11

def test_day_two() -> None:
    assert part_two(_input) == 31
