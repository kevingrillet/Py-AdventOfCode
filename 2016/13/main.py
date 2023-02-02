from collections import deque


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def fct(x, y, inpt):
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + inpt).count('1') % 2


def part_one(inpt: int) -> int:
    adjacent = ((1, 0), (-1, 0), (0, 1), (0, -1))
    stack = deque([((1, 1), 0)])
    done = set()

    while stack:
        (x, y), steps = stack.popleft()
        done.add((x, y))

        if (x, y) == (31, 39):
            return steps

        for dx, dy in adjacent:
            xx, yy = (x + dx, y + dy)
            if not ((xx, yy) in done or xx < 0 or yy < 0 or fct(xx, yy, inpt)):
                stack.append(((xx, yy), steps + 1))


def part_two(inpt: int) -> int:
    adjacent = ((1, 0), (-1, 0), (0, 1), (0, -1))
    stack = deque([((1, 1), 0)])
    done = set()

    while stack:
        (x, y), steps = stack.popleft()

        if steps > 50:
            return len(done)

        done.add((x, y))

        for dx, dy in adjacent:
            xx, yy = (x + dx, y + dy)
            if not ((xx, yy) in done or xx < 0 or yy < 0 or fct(xx, yy, inpt)):
                stack.append(((xx, yy), steps + 1))


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=int(input_string))}')
    print(f'Part two: {part_two(inpt=int(input_string))}')
