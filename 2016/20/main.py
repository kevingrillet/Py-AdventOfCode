def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    blacklist = sorted([tuple(map(int, line.split('-'))) for line in inpt])

    lowest = 0
    for (start, end) in blacklist:
        if start > lowest:
            return lowest
        lowest = max(lowest, end + 1)


def part_two(inpt: list[str]) -> int:
    blacklist = sorted([tuple(map(int, line.split('-'))) for line in inpt])

    result = 0
    lowest = 0
    for (start, end) in blacklist:
        if start > lowest:
            result += start - lowest
        lowest = max(lowest, end + 1)
    return result


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
