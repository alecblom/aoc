import argparse
import os
from app import *

def opener(path, flags):
    curr_dir = os.path.dirname(__file__)
    dir_fd = os.open(curr_dir, os.O_RDWR)
    return os.open(path, flags, dir_fd=dir_fd)

def main(day: int, test_mode: bool = True):
    curr_dir = os.path.dirname(__file__)
    # dir_fd = os.open(folder, os.O_RDWR)
    filename = "test" if test_mode else "main"
    folder = os.path.join("app", f"day_{day:02}", f"{filename}.py")
    with open(folder, 'r', opener=opener) as file:
        file.main()

def cli():
    parser = argparse.ArgumentParser(description="Run the solution for a specific day of the advent of code 2024 edition.")
    parser.add_argument("day", type=int, help="Day to execute")
    parser.add_argument(
        "--test-mode",
        "-T",
        action="store_true",
        help="Run unit test instead of real implementation",
    )
    args = parser.parse_args()
    main(args.day, args.test_mode)

if __name__ == "__main__":
    cli()