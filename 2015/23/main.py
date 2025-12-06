def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: list[str], registers: dict) -> dict:
    """Execute instructions and return final register state."""
    pos = 0
    while pos < len(inpt):
        parts = inpt[pos].split()
        instruction = parts[0]

        if instruction == "hlf":
            registers[parts[1]] //= 2
            pos += 1
        elif instruction == "tpl":
            registers[parts[1]] *= 3
            pos += 1
        elif instruction == "inc":
            registers[parts[1]] += 1
            pos += 1
        elif instruction == "jmp":
            pos += int(parts[1])
        elif instruction == "jie":
            if registers[parts[1].rstrip(",")] % 2 == 0:
                pos += int(parts[2])
            else:
                pos += 1
        elif instruction == "jio":
            if registers[parts[1].rstrip(",")] == 1:
                pos += int(parts[2])
            else:
                pos += 1

    return registers


def part_one(inpt: list[str]) -> int:
    return process(inpt, {"a": 0, "b": 0})["b"]


def part_two(inpt: list[str]) -> int:
    return process(inpt, {"a": 1, "b": 0})["b"]


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
