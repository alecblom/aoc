import argparse
import importlib
import os

# def opener(path, flags):
#     curr_dir = os.path.dirname(__file__)
#     dir_fd = os.open(curr_dir, os.O_RDWR)
#     return os.open(path, flags, dir_fd=dir_fd)

def main(day: int, test_mode: bool = True):
    exec_mode = "test" if test_mode else "main"
    module = importlib.import_module(f"app.day_{day:02}.{exec_mode}")
    module.main()

    # curr_dir = os.path.dirname(__file__)
    # # dir_fd = os.open(folder, os.O_RDWR)
    # folder = os.path.join("app", f"day_{day:02}", f"{filename}.py")
    # with open(folder, 'r', opener=opener) as file:
    #     file.main()

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