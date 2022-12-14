import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def part_one(inpt: list[str]) -> int:
    aunts = inpt.copy()

    for aunt in aunts:
        aunt_ok = True
        for key in ticker_tape:
            regex = re.compile(r'{}: (\d+)'.format(key))
            value = regex.search(aunt)
            if value:
                if int(value.group(1)) != ticker_tape[key]:
                    aunt_ok = False
                    break
        if aunt_ok:
            return int(aunt.split(' ')[1][:-1])

    return -1


def part_two(inpt: list[str]) -> int:
    aunts = inpt.copy()

    for aunt in aunts:
        aunt_ok = True
        for key in ticker_tape:
            regex = re.compile(r'{}: (\d+)'.format(key))
            value = regex.search(aunt)
            if value:
                if key in ('cats', 'trees'):
                    if int(value.group(1)) <= ticker_tape[key]:
                        aunt_ok = False
                        break
                elif key in ('pomeranians', 'goldfish'):
                    if int(value.group(1)) >= ticker_tape[key]:
                        aunt_ok = False
                        break
                else:
                    if int(value.group(1)) != ticker_tape[key]:
                        aunt_ok = False
                        break
        if aunt_ok:
            return int(aunt.split(' ')[1][:-1])

    return -1


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
