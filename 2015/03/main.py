import numpy as np


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def next_direction(dir_char: str) -> [int, int]:
    if dir_char == '^':
        return [0, 1]
    elif dir_char == 'v':
        return [0, -1]
    elif dir_char == '>':
        return [1, 0]
    elif dir_char == '<':
        return [-1, 0]
    else:
        raise ValueError('Unknow input')


def part_one(inpt: str) -> int:
    visited = [[0, 0]]
    pos = [0, 0]

    for direction in inpt:
        pos = np.add(pos, next_direction(direction)).tolist()
        if pos not in visited:
            visited.append(pos)

    return len(visited)


def part_two(inpt: str) -> int:
    visited = [[0, 0]]
    pos = [0, 0]
    pos_robot = [0, 0]
    santa = True

    for direction in inpt:
        if santa:
            pos = np.add(pos, next_direction(direction)).tolist()
            if pos not in visited:
                visited.append(pos)
        else:
            pos_robot = np.add(pos_robot, next_direction(direction)).tolist()
            if pos_robot not in visited:
                visited.append(pos_robot)

        santa = not santa

    return len(visited)


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
