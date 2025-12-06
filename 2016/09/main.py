import re


def get_example(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    """Calculate decompressed length without building the actual string."""
    marker = re.compile(r"\((\d+)x(\d+)\)")
    length = 0
    pos = 0

    while pos < len(inpt):
        reg_found = marker.search(inpt, pos)
        if not reg_found:
            # No more markers, add remaining characters
            length += len(inpt) - pos
            break

        # Add characters before the marker
        length += reg_found.start() - pos

        # Process the marker
        sub, times = map(int, reg_found.groups())
        start = reg_found.end()

        # Add the repeated section length
        length += times * sub

        # Move position past the repeated section
        pos = start + sub

    return length


def part_two(inpt: str) -> int:
    """Calculate recursively decompressed length without building the actual string."""
    marker = re.compile(r"\((\d+)x(\d+)\)")
    length = 0
    pos = 0

    while pos < len(inpt):
        reg_found = marker.search(inpt, pos)
        if not reg_found:
            # No more markers, add remaining characters
            length += len(inpt) - pos
            break

        # Add characters before the marker
        length += reg_found.start() - pos

        # Process the marker
        sub, times = map(int, reg_found.groups())
        start = reg_found.end()

        # Recursively decompress the section
        section = inpt[start : start + sub]
        section_length = part_two(section)
        length += times * section_length

        # Move position past the repeated section
        pos = start + sub

    return length


if __name__ == "__main__":
    input_example = get_example(filename="example")
    for ex in input_example:
        print(f"Example: {part_one(inpt=ex)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")

    input_example = get_example(filename="example2")
    for ex in input_example:
        print(f"Example: {part_two(inpt=ex)}")
    print(f"Part two: {part_two(inpt=input_string)}")
