import argparse

from src.helpers.executor import DayExecutor
from src.helpers.input import get_input


def main(year: int, day: int, test_mode: bool = True):
    executor = DayExecutor(year, test_mode)
    part = 0
    for result in  executor.execute(day):
        part += 1
        print(f"Answer part {part}: {result}")


def cli():
    parser = argparse.ArgumentParser(description="Run the solution for a specific day of the advent of code 2024 edition.")
    parser.add_argument("year", type=int, help="Year to execute")
    parser.add_argument("day", type=int, help="Day to execute")
    parser.add_argument(
        "--test-mode",
        "-T",
        action="store_true",
        help="Run unit test instead of real implementation",
    )
    args = parser.parse_args() 
    main(args.year, args.day, args.test_mode)


if __name__ == "__main__":
    cli()