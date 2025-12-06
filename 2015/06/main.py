import re

import numpy as np

# Grid size: 1000x1000 lights numbered from 0 to 999 in each direction
GRID_SIZE = 1000


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def parse_coords(line: str) -> tuple[int, int, int, int]:
    """Extract coordinates from instruction line."""
    regex_coord = re.compile(r"(\d+),(\d+) through (\d+),(\d+)")
    match = regex_coord.search(line)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())
        return x1, y1, x2, y2
    raise ValueError(f"Invalid coordinate format in line: {line}")


def part_one(inpt: list[str]) -> int:
    lights = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)

    for line in inpt:
        x1, y1, x2, y2 = parse_coords(line)

        if "turn on" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] = True
        elif "turn off" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] = False
        elif "toggle" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] = ~lights[x1 : x2 + 1, y1 : y2 + 1]

    return np.count_nonzero(lights)


def part_two(inpt: list[str]) -> int:
    lights = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    for line in inpt:
        x1, y1, x2, y2 = parse_coords(line)

        if "turn on" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] += 1
        elif "turn off" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] = np.maximum(lights[x1 : x2 + 1, y1 : y2 + 1] - 1, 0)
        elif "toggle" in line:
            lights[x1 : x2 + 1, y1 : y2 + 1] += 2

    return int(np.sum(lights))


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
