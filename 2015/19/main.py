import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    molecule = inpt[-1]
    replacements = inpt[:-2]

    result = set()
    for replacement in replacements:
        molecule_from, molecule_to = replacement.split(" => ")

        pos = 0
        while pos < len(molecule):
            if molecule[pos : pos + len(molecule_from)] == molecule_from:
                result.add(
                    molecule[:pos] + molecule_to + molecule[pos + len(molecule_from) :]
                )
                pos += len(molecule_from)
            else:
                pos += 1

    return len(result)


def part_two(inpt: list[str]) -> int:
    molecule = inpt[-1][::-1]
    replacements = inpt[:-2]

    reverse = {}
    for replacement in replacements:
        molecule_from, molecule_to = replacement.split(" => ")
        reverse[molecule_to[::-1]] = molecule_from[::-1]

    result = 0
    while molecule != "e":
        # Need to reverse the keys to match the biggest molecules possible,
        # but multiple letters molecule require molecule to be reversed too...
        molecule = re.sub(
            "|".join(reversed(reverse.keys())),
            lambda m: reverse[m.group()],
            molecule,
            1,
        )
        result += 1
        # print(molecule)
        # if result >= 100:
        #     exit(1)

    return result


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example one: {part_one(inpt=input_string)}")
    input_string = get_input(filename="example2")
    print(f"Example two: {part_two(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
