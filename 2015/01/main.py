def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    return inpt.count("(") - inpt.count(")")


def part_two(inpt: str) -> int:
    level = 0
    for position, char in enumerate(inpt, 1):
        level += 1 if char == "(" else -1
        if level == -1:
            return position
    return -1


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
