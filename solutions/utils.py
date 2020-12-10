def read_file_int(day):
    lines = []
    with open(f"./inputs/input{day}.txt", "r") as f:

        for line in f.readlines():
            lines.append(int(line.rstrip()))

    return lines


def read_file(day):
    return list(map(str.strip, open(f"./inputs/input{day}.txt", "r")))
