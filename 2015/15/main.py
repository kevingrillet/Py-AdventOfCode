import re
from collections.abc import Generator
from math import prod

TARGET_CALORIES = 500


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def generate_mixtures(number_of_ingredients: int, sum_teaspoons: int) -> Generator[list[int], None, None]:
    """Generate all possible mixtures of ingredients."""
    if number_of_ingredients == 1:
        yield [sum_teaspoons]
    else:
        for teaspoon in range(sum_teaspoons + 1):
            for rest in generate_mixtures(number_of_ingredients - 1, sum_teaspoons - teaspoon):
                yield [teaspoon] + rest


def parse_ingredients(inpt: list[str]) -> list[list[int]]:
    """Parse ingredients into stats list."""
    regex = re.compile(r"\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
    result = []
    for line in inpt:
        match = regex.search(line)
        if match:
            result.append(list(map(int, match.groups())))
    return result


def calculate_score(mix: list[int], stats: list[list[int]], check_calories: bool = False) -> int:
    """Calculate cookie score for a given mixture."""
    properties = [sum(mix[i] * stats[i][j] for i in range(len(mix))) for j in range(5)]

    # Check if any property is negative
    if any(p <= 0 for p in properties[:4]):
        return 0

    # Check calories constraint
    if check_calories and properties[4] != TARGET_CALORIES:
        return 0

    return prod(properties[:4])


def part_one(inpt: list[str]) -> int:
    stats = parse_ingredients(inpt)
    return max(calculate_score(mix, stats) for mix in generate_mixtures(len(stats), 100))


def part_two(inpt: list[str]) -> int:
    stats = parse_ingredients(inpt)
    return max(calculate_score(mix, stats, True) for mix in generate_mixtures(len(stats), 100))


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
