import itertools
from math import prod


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def find_min_qe(packages: list[int], nb_groups: int) -> int:
    """Find minimum quantum entanglement for optimal grouping."""
    group_weight = sum(packages) // nb_groups

    # Find smallest group size that works
    for size in range(1, len(packages)):
        valid_combos = [combo for combo in itertools.combinations(packages, size) if sum(combo) == group_weight]

        if valid_combos:
            return min(prod(combo) for combo in valid_combos)

    return 0


def part_one(inpt: list[int]) -> int:
    return find_min_qe(inpt, 3)


def part_two(inpt: list[int]) -> int:
    return find_min_qe(inpt, 4)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    input_int = list(map(int, input_string))
    print(f"Part one: {part_one(inpt=input_int)}")
    print(f"Part two: {part_two(inpt=input_int)}")
