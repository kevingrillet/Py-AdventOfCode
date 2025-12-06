import re
from typing import Optional

MAX_USED_SIZE = 100


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


def part_one(inpt: list[str]) -> int:
    result = 0
    for node1 in inpt[2:]:
        used = int(node1.split()[2][:-1])
        if used == 0:
            continue

        for node2 in inpt[2:]:
            avail = int(node2.split()[3][:-1])
            if avail >= used and node1 != node2:
                result += 1
    return result


def part_two(inpt: list[str]) -> int:
    grid: list[list[str]] = []
    regex = re.compile(r"x(\d+)-y(\d+).+T\s+(\d+)T\s+(\d+)T\s+\d+%")
    for node_str in inpt[2:]:
        match = regex.search(node_str)
        if not match:
            continue
        x, y, used, _ = map(int, match.groups())

        if y > len(grid) - 1:
            for _ in range(len(grid) - 1, y):
                grid.append([])

        if x > len(grid[y]) - 1:
            for _ in range(len(grid[y]) - 1, x):
                grid[y].append(".")

        if (x, y) == (0, 0):
            grid[y][x] = "O"
        elif used > MAX_USED_SIZE:
            grid[y][x] = "#"
        elif used == 0:
            grid[y][x] = "_"

    grid[0][-1] = "G"

    # Half Manual solution...
    # for line in grid:
    #     print(' '.join(line))

    steps: int = 0
    node: Optional[tuple[int, int]] = None
    pb: Optional[tuple[int, int]] = None
    for index, line in enumerate(grid):
        if "#" in line:
            pb = (index, line.index("#"))
        if "_" in line:
            node = (index, line.index("_"))
    goal: tuple[int, int] = (0, grid[0].index("G"))

    if node and pb:
        p1: tuple[int, int] = (pb[0], pb[1] - 1)
        steps += manhattan(node, p1)
        steps += manhattan(p1, goal)
        steps += 5 * (goal[1] - 1)

    return steps


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
