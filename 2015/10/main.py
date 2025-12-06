from itertools import groupby


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def look_and_say(sequence: str) -> str:
    """Apply look-and-say transformation to a sequence."""
    return "".join(f"{len(list(group))}{digit}" for digit, group in groupby(sequence))


def process(inpt: str, times: int) -> str:
    """Apply look-and-say transformation multiple times."""
    sequence = inpt
    for _ in range(times):
        sequence = look_and_say(sequence)
    return sequence


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {len(process(inpt=input_string, times=40))}")
    print(f"Part two: {len(process(inpt=input_string, times=50))}")
