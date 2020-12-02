def read_file_int(day):
    lines = []
    with open(f"./inputs/input{day}.txt", "r") as f:

        for line in f.readlines():
            lines.append(int(line.rstrip()))

    return lines


def read_file(day):
    with open(f"./inputs/input{day}.txt", "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
