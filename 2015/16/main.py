import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_aunt(line: str) -> tuple[int, dict]:
    """Parse aunt line and return number and attributes dict."""
    number_match = re.search(r"Sue (\d+):", line)
    if not number_match:
        return -1, {}
    number = int(number_match.group(1))
    attrs = {}
    for match in re.finditer(r"(\w+): (\d+)", line):
        attrs[match.group(1)] = int(match.group(2))
    return number, attrs


def part_one(inpt: list[str]) -> int:
    for line in inpt:
        number, attrs = parse_aunt(line)
        if all(attrs.get(key, value) == value for key, value in TICKER_TAPE.items()):
            return number
    return -1


def part_two(inpt: list[str]) -> int:
    for line in inpt:
        number, attrs = parse_aunt(line)
        match = True
        for key, expected in TICKER_TAPE.items():
            if key not in attrs:
                continue
            actual = attrs[key]
            if key in ("cats", "trees"):
                if actual <= expected:
                    match = False
                    break
            elif key in ("pomeranians", "goldfish"):
                if actual >= expected:
                    match = False
                    break
            elif actual != expected:
                match = False
                break
        if match:
            return number
    return -1


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
