import itertools
import re
from collections import defaultdict


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def parse_happiness(inpt: list[str]) -> tuple[set, dict]:
    """Parse input and return set of persons and happiness dict."""
    regex = re.compile(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).")
    happiness = defaultdict(dict)
    persons = set()

    for line in inpt:
        match = regex.search(line)
        if not match:
            continue
        person1, action, value, person2 = match.groups()
        persons.add(person1)
        happiness[person1][person2] = int(value) * (1 if action == "gain" else -1)

    return persons, happiness


def calculate_optimal_happiness(persons: set, happiness: dict) -> int:
    """Calculate the maximum happiness for all seating arrangements."""
    best_happiness = 0

    for arrangement in itertools.permutations(persons):
        total = sum(
            happiness[arrangement[i]].get(arrangement[(i + 1) % len(arrangement)], 0)
            + happiness[arrangement[(i + 1) % len(arrangement)]].get(arrangement[i], 0)
            for i in range(len(arrangement))
        )
        best_happiness = max(best_happiness, total)

    return best_happiness


def part_one(inpt: list[str]) -> int:
    persons, happiness = parse_happiness(inpt)
    return calculate_optimal_happiness(persons, happiness)


def part_two(inpt: list[str]) -> int:
    persons, happiness = parse_happiness(inpt)
    persons.add("me")
    return calculate_optimal_happiness(persons, happiness)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    # Aswer two it the value itself, not the "total change"...
    print(f"Part two: {part_two(inpt=input_string)}")
