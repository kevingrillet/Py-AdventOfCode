def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    level = 0
    for char in inpt:
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        else:
            raise ValueError("Unknow input")
    return level


def part_two(inpt: str) -> int:
    level = 0
    position = 0
    for char in inpt:
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        position += 1
        if level <= -1:
            return position


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
