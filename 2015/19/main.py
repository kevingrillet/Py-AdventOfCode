import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    """Find all unique molecules after one replacement."""
    molecule = inpt[-1]
    replacements = inpt[:-2]

    result = set()
    for replacement in replacements:
        molecule_from, molecule_to = replacement.split(" => ")

        # Find all occurrences of molecule_from and replace each one
        pos = 0
        while pos < len(molecule):
            if molecule[pos : pos + len(molecule_from)] == molecule_from:
                new_molecule = molecule[:pos] + molecule_to + molecule[pos + len(molecule_from) :]
                result.add(new_molecule)
                pos += len(molecule_from)
            else:
                pos += 1

    return len(result)


def part_two(inpt: list[str]) -> int:
    """Find minimum steps to create molecule from 'e'.

    Uses greedy approach with reversed strings to prioritize
    replacing larger molecules first (greedily reduce complexity).
    """
    molecule = inpt[-1][::-1]
    replacements = inpt[:-2]

    # Reverse all replacements
    reverse = {
        molecule_to[::-1]: molecule_from[::-1]
        for replacement in replacements
        for molecule_from, molecule_to in [replacement.split(" => ")]
    }

    result = 0
    while molecule != "e":
        # Replace the first matching (largest) molecule
        molecule = re.sub(
            "|".join(reversed(reverse.keys())),
            lambda m: reverse[m.group()],
            molecule,
            count=1,
        )
        result += 1

    return result


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example one: {part_one(inpt=input_string)}")
    input_string = get_input(filename="example2")
    print(f"Example two: {part_two(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
