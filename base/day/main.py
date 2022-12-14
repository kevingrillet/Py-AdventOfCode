def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        # return f.read().strip()
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    pass


def part_two(inpt: list[str]) -> int:
    pass


if __name__ == '__main__':
    # input_string = get_input(filename='example')
    # print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
