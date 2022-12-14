import time

import numpy as np


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str, implementation: int) -> int:
    objective = int(inpt)

    if implementation == 1:
        # /!\ WRONG & slow (30s after 100k)
        factors = set()
        door = 0
        while True:
            door += 1
            factors_at_door = set()
            for factor in factors:
                if factor > 1 and door % factor == 0:
                    factors_at_door.add(factor)
            if not any(factors_at_door):
                factors.add(door)
                factors_at_door.add(door)
            factors_at_door.add(1)
            if sum([present * 10 for present in factors_at_door]) >= objective:
                return door

            # print(f'House {door} got {sum([present * 10 for present in factors_at_door])} presents.')
            # print(factors_at_door)
            # if door % 10000 == 0:
            #     print(door)
            # if door == 10:
            # if door == 100000:
            #     break

    elif implementation == 2:
        # RIGHT but SLOW (4min after 100k)
        door = 0
        while True:
            door += 1
            factors_at_door = set()
            for factor in range(1, door + 1):
                if door % factor == 0:
                    factors_at_door.add(factor)

            if sum([present * 10 for present in factors_at_door]) >= objective:
                return door

            # print(f'House {door} got {sum([present * 10 for present in factors_at_door])} presents.')
            # print(factors_at_door)
            # if door % 10000 == 0:
            #     print(door)
            # if door == 10:
            # if door == 100000:
            #     break

    elif implementation == 3:
        doors = np.full(objective // 10, 10, int)
        for factor in range(2, objective // 10):
            for door in range(factor, objective // 10, factor):
                doors[door] += factor * 10

        # print(doors[:10])

        for door, present in enumerate(doors):
            if present > objective:
                return door

    return -1


def part_two(inpt: str) -> int:
    objective = int(inpt)
    doors = np.full(objective // 10, 11, int)
    for factor in range(2, objective // 10):
        for door in range(factor, objective // 10, factor)[:50]:
            doors[door] += factor * 11

    # print(doors[:10])

    for door, present in enumerate(doors):
        if present > objective:
            return door


if __name__ == '__main__':
    input_string = get_input(filename='input')
    st = time.time()
    print(f'Part one: {part_one(inpt=input_string, implementation=3)}')
    print(f'Execution time: {time.time() - st} seconds')
    st = time.time()
    print(f'Part two: {part_two(inpt=input_string)}')
    print(f'Execution time: {time.time() - st} seconds')
