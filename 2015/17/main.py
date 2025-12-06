import itertools

# Total liters of eggnog to store
EGGNOG_LITERS = 150


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    containers = list(map(int, inpt))
    return sum(
        1
        for nb in range(len(containers))
        for combo in itertools.combinations(containers, nb)
        if sum(combo) == EGGNOG_LITERS
    )


def part_two(inpt: list[str]) -> int:
    containers = list(map(int, inpt))
    for nb in range(len(containers)):
        count = sum(1 for combo in itertools.combinations(containers, nb) if sum(combo) == EGGNOG_LITERS)
        if count > 0:
            return count
    return 0


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
