def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    lines = inpt.copy()
    result = 0
    for line in lines:
        # literals
        result += len(line)

        line = line.strip()[1:-1]

        i = 0
        while i < len(line):
            # in memory
            result -= 1
            if line[i] == '\\':
                if line[i + 1] == 'x':
                    i += 4
                else:
                    i += 2
            else:
                i += 1

    return result


def part_two(inpt: list[str]) -> int:
    lines = inpt.copy()
    result = 0
    for line in lines:
        # literals
        result -= len(line)

        # outer "
        result += 2

        for char in line:
            if char in ('\\', '"'):
                result += 2
            else:
                result += 1

    return result


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
