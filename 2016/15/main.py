def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        # return f.read().strip()
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    discs = []
    for line in inpt:
        splt = line.split(" ")
        discs.append([int(splt[3]), int(splt[-1][:-1])])

    time = 0

    while True:
        if not sum((disc[1] + index + time) % disc[0] for (index, disc) in enumerate(discs, 1)):
            return time
        time += 1


def part_two(inpt: list[str]) -> int:
    discs = []
    for line in inpt:
        splt = line.split(" ")
        discs.append([int(splt[3]), int(splt[-1][:-1])])

    discs.append([11, 0])

    time = 0

    while True:
        if not sum((disc[1] + position + time) % disc[0] for (position, disc) in enumerate(discs, 1)):
            return time
        time += 1


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
