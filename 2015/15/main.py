import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def generate_mixtures(number_of_ingredients: int, sum_teaspoons: int) -> [int]:
    for teaspoon in range(sum_teaspoons if number_of_ingredients == 1 else 0, sum_teaspoons + 1):
        difference = sum_teaspoons - teaspoon
        if number_of_ingredients - 1:
            for y in generate_mixtures(number_of_ingredients - 1, difference):
                yield [teaspoon] + y
        else:
            yield [teaspoon]


def part_one(inpt: list[str]) -> int:
    result = 0
    regex = re.compile(
        r'\w*: capacity ([0-9-]+), durability ([0-9-]+), flavor ([0-9-]+), texture ([0-9-]+), calories ([0-9-]+)')

    stats = []
    for ingredient in inpt:
        stats.append(list(map(int, regex.search(ingredient).groups())))

    # I don't like this solution... but I don't have anything better atm :/
    # for i1 in range(0, 101):
    #     for i2 in range(0, 101 - i1):
    #         for i3 in range(0, 101 - i1 - i2):
    #             i4 = 100 - (i1 + i2 + i3)
    #             tc = i1 * stats[0][0] + i2 * stats[1][0] + i3 * stats[2][0] + i4 * stats[3][0]
    #             td = i1 * stats[0][1] + i2 * stats[1][1] + i3 * stats[2][1] + i4 * stats[3][1]
    #             tf = i1 * stats[0][2] + i2 * stats[1][2] + i3 * stats[2][2] + i4 * stats[3][2]
    #             tt = i1 * stats[0][3] + i2 * stats[1][3] + i3 * stats[2][3] + i4 * stats[3][3]
    #
    #             if tc <= 0 or td <= 0 or tf <= 0 or tt <= 0:
    #                 continue
    #
    #             score = tc * td * tf * tt
    #             if score > result:
    #                 result = score

    # Better solution :)
    for mix in list(generate_mixtures(len(stats), 100)):
        ingredient = 0
        tc = td = tf = tt = 0
        while ingredient < len(stats):
            tc += mix[ingredient] * stats[ingredient][0]
            td += mix[ingredient] * stats[ingredient][1]
            tf += mix[ingredient] * stats[ingredient][2]
            tt += mix[ingredient] * stats[ingredient][3]
            ingredient += 1

        if tc <= 0 or td <= 0 or tf <= 0 or tt <= 0:
            continue

        score = tc * td * tf * tt
        if score > result:
            result = score

    return result


def part_two(inpt: list[str]) -> int:
    result = 0
    regex = re.compile(
        r'\w*: capacity ([0-9-]+), durability ([0-9-]+), flavor ([0-9-]+), texture ([0-9-]+), calories ([0-9-]+)')

    stats = []
    for ingredient in inpt:
        stats.append(list(map(int, regex.search(ingredient).groups())))

    for mix in list(generate_mixtures(len(stats), 100)):
        ingredient = 0
        tc = td = tf = tt = c2 = 0
        while ingredient < len(stats):
            tc += mix[ingredient] * stats[ingredient][0]
            td += mix[ingredient] * stats[ingredient][1]
            tf += mix[ingredient] * stats[ingredient][2]
            tt += mix[ingredient] * stats[ingredient][3]
            c2 += mix[ingredient] * stats[ingredient][4]
            ingredient += 1

        if tc <= 0 or td <= 0 or tf <= 0 or tt <= 0:
            continue

        if c2 != 500:
            continue

        score = tc * td * tf * tt
        if score > result:
            result = score

    return result


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
