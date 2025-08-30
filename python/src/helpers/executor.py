import importlib
from src.helpers.core import get_input

class DayExecutor:
    def __init__(self, year: int, test_mode: bool = True):
        self._year = year
        self._test_mode = test_mode

    def execute(self, day: int):
        input_data = get_input(self._year, day, example=self._test_mode)
        module = importlib.import_module(f"src.year_{self._year}.day_{day:02}.main")
        return module.main(input_data)