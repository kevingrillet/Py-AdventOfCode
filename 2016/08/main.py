import re

import numpy as np
from numpy import ndarray


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str], grid: ndarray) -> int:
    for cmd in inpt:
        if 'rect' in cmd:
            w, h = map(int, re.search(r'(\d+)x(\d+)', cmd).groups())
            grid[:h, :w] = '#'
        elif 'row' in cmd:
            y, p = map(int, re.search(r'y=(\d+) by (\d+)', cmd).groups())
            grid[y] = np.roll(grid[y], p)
        elif 'column' in cmd:
            x, p = map(int, re.search(r'x=(\d+) by (\d+)', cmd).groups())
            grid[:, x] = np.roll(grid[:, x], p)
    print('\n'.join(' '.join(str(x) for x in row) for row in grid))
    print('')
    return np.count_nonzero(grid == '#')


def part_two(inpt: list[str]) -> int:
    pass


if __name__ == '__main__':
    global_grid = np.full((3, 7), '.', str)
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string, grid=global_grid)}')

    global_grid = np.full((6, 50), '.', str)
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string, grid=global_grid)}')
    # print(f'Part two: {part_two(inpt=input_string)}')
