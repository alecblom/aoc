import os

INPUTS_DIR = "../inputs"

def get_input(year: int, day: int, example: bool = False) -> str:
    file_name = "example.txt" if example else "input.txt"
    file_location = os.path.join(INPUTS_DIR, str(year), f"{day:02}", file_name)

    with open(file_location) as file:
        return file.read()
