import re


def get_example(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> str:
    marker = re.compile(r'\((\d+)x(\d+)\)')
    reg_found = marker.search(inpt)
    if not reg_found:
        return inpt
    sub, times = map(int, reg_found.groups())
    start = reg_found.start() + len(reg_found.group())
    return inpt[:reg_found.start()] + times * inpt[start:start+sub] + part_one(inpt[start + sub:])


def part_two(inpt: str) -> str:
    marker = re.compile(r'\((\d+)x(\d+)\)')
    reg_found = marker.search(inpt)
    if not reg_found:
        return inpt
    sub, times = map(int, reg_found.groups())
    start = reg_found.start() + len(reg_found.group())
    return inpt[:reg_found.start()] + times * part_two(inpt[start:start+sub]) + part_two(inpt[start + sub:])


if __name__ == '__main__':
    input_example = get_example(filename='example')
    for ex in input_example:
        print(f'Example: {len(part_one(inpt=ex))}')

    input_string = get_input(filename='input')
    print(f'Part one: {len(part_one(inpt=input_string))}')

    input_example = get_example(filename='example2')
    for ex in input_example:
        print(f'Example: {len(part_two(inpt=ex))}')
    print(f'Part two: {len(part_two(inpt=input_string))}')
