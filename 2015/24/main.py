import itertools


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: list[int], nb_group: int) -> int:
    group_weight = sum(inpt) // nb_group
    group_smallest = len(inpt)
    group_best = []

    cpt = 0
    while cpt < len(inpt):
        cpt += 1
        if cpt > group_smallest:
            break

        combinations = itertools.combinations(inpt, cpt)
        for combination in combinations:
            if sum(combination) == group_weight:
                group_best.append(list(combination))
                group_smallest = cpt

    result = max(inpt) ** len(inpt)

    for combination in group_best:
        qe = 1
        for weight in combination:
            qe *= weight

        result = min(result, qe)

    return result


def part_one(inpt: list[int]) -> int:
    return process(inpt, 3)


def part_two(inpt: list[int]) -> int:
    return process(inpt, 4)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    input_int = list(map(int, input_string))
    print(f"Part one: {part_one(inpt=input_int)}")
    print(f"Part two: {part_two(inpt=input_int)}")
