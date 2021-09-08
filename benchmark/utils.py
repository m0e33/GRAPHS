def count_lines(path):
    with open(path, "r") as file:
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        return len(nonempty_lines)
