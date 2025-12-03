import numpy as np


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    result = 0
    for line in inpt:
        sides = []
        length, width, height = map(int, line.split("x"))
        sides.append(2 * length * width)
        sides.append(2 * width * height)
        sides.append(2 * height * length)
        for side in sides:
            result += side
        # Slack
        result += min(sides) // 2

    return result


def part_two(inpt: list[str]) -> int:
    result = 0
    for line in inpt:
        sides = sorted(map(int, line.split("x")))
        # Wrap
        result += sides[0] * 2 + sides[1] * 2
        # Bow
        result += np.prod(sides)
    return result


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
