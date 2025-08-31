import os

INPUTS_DIR = "../inputs"

def get_input(year: int, day: int) -> str:
    file_location = os.path.join(INPUTS_DIR, str(year), f"{day:02}", "input.txt")

    with open(file_location) as file:
        return file.read()
