import itertools
import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: str, p1: str, p2: str) -> int:
    r1 = re.compile(r'{} would (gain|lose) (\d+) happiness units by sitting next to {}.'.format(p1, p2))
    r2 = re.compile(r'{} would (gain|lose) (\d+) happiness units by sitting next to {}.'.format(p2, p1))

    e1, v1 = map(str, r1.search(inpt).groups())
    e2, v2 = map(str, r2.search(inpt).groups())

    return int(v1) * (1 if e1 == 'gain' else -1) + int(v2) * (1 if e2 == 'gain' else -1)


def part_one(inpt: list[str]) -> int:
    potential = ''.join(inpt)

    persons = []
    for line in inpt:
        person = line.split(' ')[0]
        if person not in persons:
            persons.append(person)

    permutations = list(itertools.permutations(persons))

    happiest = 0
    for perm in permutations:
        happiness = 0

        pos = 0
        while pos < len(perm):
            happiness += process(potential, perm[pos], perm[pos + 1 if pos < len(perm) - 1 else 0])
            pos += 1

        if happiness > happiest:
            happiest = happiness

    return happiest


def part_two(inpt: list[str]) -> int:
    potential = ''.join(inpt)

    persons = ['me']
    for line in inpt:
        person = line.split(' ')[0]
        if person not in persons:
            persons.append(person)

    permutations = list(itertools.permutations(persons))

    happiest = 0
    for perm in permutations:
        happiness = 0

        pos = 0
        while pos < len(perm):
            if perm[pos] != 'me' and perm[pos + 1 if pos < len(perm) - 1 else 0] != 'me':
                happiness += process(potential, perm[pos], perm[pos + 1 if pos < len(perm) - 1 else 0])
            pos += 1

        if happiness > happiest:
            happiest = happiness

    return happiest


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    # Aswer two it the value itself, not the "total change"...
    print(f'Part two: {part_two(inpt=input_string)}')
