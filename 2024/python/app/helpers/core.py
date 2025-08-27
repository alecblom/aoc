def get_input(day: int, example: bool = False) -> str:
    file_name = "example.txt" if example else "input.txt"
    file_location = f"../inputs/{day:02}/{file_name}"
    file = open(file_location)
    content = file.read()
    file.close()
    return content
