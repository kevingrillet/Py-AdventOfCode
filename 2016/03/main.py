import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    result = 0
    regex = re.compile(r'(\d+)')

    for triangle in inpt:
        a, b, c = sorted(list(map(int, regex.findall(triangle))))
        if a + b > c:
            result += 1
    return result


def part_two(inpt: list[str]) -> int:
    result = 0
    regex = re.compile(r'(\d+)')

    pos = 0
    while pos < len(inpt):
        a, b, c = list(map(int, regex.findall(inpt[pos])))
        a1, b1, c1 = list(map(int, regex.findall(inpt[pos + 1])))
        a2, b2, c2 = list(map(int, regex.findall(inpt[pos + 2])))

        triangles = [sorted([a, a1, a2]), sorted([b, b1, b2]), sorted([c, c1, c2])]
        for triangle in triangles:
            if triangle[0] + triangle[1] > triangle[2]:
                result += 1

        pos += 3

    return result


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Example:', part_two(inpt=get_input(filename='example')))
    print(f'Part two: {part_two(inpt=input_string)}')
