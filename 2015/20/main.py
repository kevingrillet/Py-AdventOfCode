import numpy as np


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    """Find first house with at least target presents (10 per elf)."""
    objective = int(inpt)
    max_house = objective // 10
    houses = np.full(max_house, 10, dtype=int)

    for elf in range(2, max_house):
        houses[elf::elf] += elf * 10

    return int(np.argmax(houses >= objective))


def part_two(inpt: str) -> int:
    """Find first house with at least target presents (11 per elf, max 50 houses per elf)."""
    objective = int(inpt)
    max_house = objective // 10
    houses = np.full(max_house, 11, dtype=int)

    for elf in range(2, max_house):
        houses[elf : min(elf * 51, max_house) : elf] += elf * 11

    return int(np.argmax(houses >= objective))


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
