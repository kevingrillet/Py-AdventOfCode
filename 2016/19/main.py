import numpy as np


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: int) -> int:
    elves = np.arange(inpt)
    while True:
        nb = len(elves)
        if nb <= 2:
            return elves[0] + 1
        # elves = np.roll(np.delete(elves, 1), -1)
        if nb % 2:
            elves = np.roll(elves[::2], 1)
        else:
            elves = elves[::2]


def part_two(inpt: int) -> int:
    elves = np.arange(inpt)
    while True:
        nb = len(elves)
        if nb <= 2:
            return elves[0] + 1
        # elves = np.roll(np.delete(elves, (nb // 2)), -1)
        middle = nb // 2
        if nb % 2:
            elves = np.roll(np.roll(elves, -middle)[1::3], middle - (nb - (nb + 1) // 3))
        else:
            elves = np.roll(np.roll(elves, -middle)[2::3], middle - (nb - nb // 3))


if __name__ == '__main__':
    input_int = int(get_input(filename='example'))
    print(f'Example one: {part_one(inpt=input_int)}')
    print(f'Example two: {part_two(inpt=input_int)}')

    input_int = int(get_input(filename='input'))
    print(f'Part one: {part_one(inpt=input_int)}')
    print(f'Part two: {part_two(inpt=input_int)}')
