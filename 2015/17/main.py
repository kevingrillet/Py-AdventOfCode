import itertools


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    containers = list(map(int, inpt))

    result = 0
    for nb in range(len(containers)):
        for combination in itertools.combinations(containers, nb):
            if sum(combination) == 150:
                result += 1

    return result


def part_two(inpt: list[str]) -> int:
    containers = list(map(int, inpt))

    result = 0
    for nb in range(len(containers)):
        for combination in itertools.combinations(containers, nb):
            if sum(combination) == 150:
                result += 1
        if result != 0:
            break

    return result


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
