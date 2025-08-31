import importlib
from src.helpers.input import get_input

class DayExecutor:
    def __init__(self, year: int, test_mode: bool = True):
        self._year = year
        self._test_mode = test_mode

    def execute(self, day: int):
        module = importlib.import_module(f"src.year_{self._year}.day_{day:02}")
        if not self._test_mode:
            input_data = get_input(self._year, day)
            return module.main(input_data)
        else:
            return module.part_one(), module.part_two()
