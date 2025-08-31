import pytest
from src.helpers.executor import DayExecutor

@pytest.fixture(name="executor_2024")
def fxt_executor_2024():
    return DayExecutor(year=2024, test_mode=True)