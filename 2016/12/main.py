from collections import defaultdict


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    instructions = defaultdict(int)

    index = 0
    while index < len(inpt):
        parse = inpt[index].split()
        if parse[0] == 'cpy':
            if parse[1].isdigit():
                instructions[parse[2]] = int(parse[1])
            else:
                instructions[parse[2]] = instructions[parse[1]]
        elif parse[0] == 'inc':
            instructions[parse[1]] += 1
        elif parse[0] == 'dec':
            instructions[parse[1]] -= 1
        elif parse[0] == 'jnz':
            if parse[1].isdigit():
                if parse[1] != 0:
                    index += int(parse[2])
                    continue
            elif instructions[parse[1]] != 0:
                index += int(parse[2])
                continue
        index += 1

    return instructions['a']


def part_two(inpt: list[str]) -> int:
    instructions = defaultdict(int)
    instructions['c'] = 1

    index = 0
    while index < len(inpt):
        parse = inpt[index].split()
        if parse[0] == 'cpy':
            if parse[1].isdigit():
                instructions[parse[2]] = int(parse[1])
            else:
                instructions[parse[2]] = instructions[parse[1]]
        elif parse[0] == 'inc':
            instructions[parse[1]] += 1
        elif parse[0] == 'dec':
            instructions[parse[1]] -= 1
        elif parse[0] == 'jnz':
            if parse[1].isdigit():
                if parse[1] != 0:
                    index += int(parse[2])
                    continue
            elif instructions[parse[1]] != 0:
                index += int(parse[2])
                continue
        index += 1

    return instructions['a']


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
