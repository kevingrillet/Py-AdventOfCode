from collections import deque
from hashlib import md5


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def run(inpt: str) -> (str, int):
    solutions = []
    rooms = deque([((0, 0), '')])

    while rooms:
        pos, path = rooms.popleft()

        if pos == (3, 3):
            solutions.append(path)
            continue

        u, d, l, r = md5((inpt+path).encode()).hexdigest()[:4]
        if u > 'a' and pos[1] > 0:
            rooms.append(((pos[0], pos[1] - 1), path + 'U'))
        if d > 'a' and pos[1] < 3:
            rooms.append(((pos[0], pos[1] + 1), path + 'D'))
        if l > 'a' and pos[0] > 0:
            rooms.append(((pos[0] - 1, pos[1]), path + 'L'))
        if r > 'a' and pos[0] < 3:
            rooms.append(((pos[0] + 1, pos[1]), path + 'R'))

    return solutions[0], len(solutions[-1])


if __name__ == '__main__':
    # input_string = get_input(filename='example')
    # print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    solution, length = run(inpt=input_string)
    print(f'Part one: {solution}')
    print(f'Part two: {length}')
