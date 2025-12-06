from math import prod


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    result = 0
    for line in inpt:
        length, width, height = map(int, line.split("x"))
        sides = [length * width, width * height, height * length]
        result += 2 * sum(sides) + min(sides)
    return result


def part_two(inpt: list[str]) -> int:
    result = 0
    for line in inpt:
        dimensions = sorted(map(int, line.split("x")))
        # Wrap: smallest perimeter
        result += 2 * (dimensions[0] + dimensions[1])
        # Bow: volume
        result += prod(dimensions)
    return result


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
