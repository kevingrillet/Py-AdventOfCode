import re

import numpy as np

# Grid size: 1000x1000 lights numbered from 0 to 999 in each direction
GRID_SIZE = 1000


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    lights = np.full((GRID_SIZE, GRID_SIZE), False, dtype=bool)
    regex_coord = re.compile(r"(\d*),(\d*) through (\d*),(\d*)")

    for line in inpt:
        x1, y1, x2, y2 = map(int, regex_coord.findall(line)[0])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if "on" in line:
                    lights[x][y] = True
                elif "off" in line:
                    lights[x][y] = False
                elif "toggle" in line:
                    lights[x][y] = not lights[x][y]

    return np.count_nonzero(lights)


def part_two(inpt: list[str]) -> int:
    lights = np.zeros((GRID_SIZE, GRID_SIZE))
    regex_coord = re.compile(r"(\d*),(\d*) through (\d*),(\d*)")

    for line in inpt:
        x1, y1, x2, y2 = map(int, regex_coord.findall(line)[0])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if "on" in line:
                    lights[x][y] += 1
                elif "off" in line:
                    if lights[x][y] > 0:
                        lights[x][y] -= 1
                elif "toggle" in line:
                    lights[x][y] += 2

    return int(np.sum(lights))


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
