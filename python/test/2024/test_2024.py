import pytest
from src.helpers.executor import DayExecutor


@pytest.mark.parametrize(
    "day,expected",
    [
        (1, (11, 31)),
    ])
def test_all_days(
    day: int,
    expected: tuple[int, int],
    executor_2024: DayExecutor
):
    result_part_one, result_part_two = executor_2024.execute(day=day)
    assert result_part_one == expected[0], f"Day {day} part one failed"
    assert result_part_two == expected[1], f"Day {day} part two failed"
