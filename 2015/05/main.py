import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    result = 0
    regex_vowels = re.compile(r'([aeiou].*){3,}')
    regex_double = re.compile(r'(.)\1')
    regex_disallowed = re.compile(r'ab|cd|pq|xy')
    for line in inpt:
        if regex_vowels.search(line) and regex_double.search(line) and not regex_disallowed.search(line):
            result += 1
    return result


def part_two(inpt: list[str]) -> int:
    result = 0
    regex_pair = re.compile(r'(..).*\1')
    regex_between = re.compile(r'(.).\1')
    for line in inpt:
        if regex_pair.search(line) and regex_between.search(line):
            result += 1
    return result


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
