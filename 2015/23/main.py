def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: list[str], registers: dict) -> dict:
    pos = 0
    while pos < len(inpt):
        splt = inpt[pos].split(" ")

        if splt[0] == "hlf":
            registers[splt[1]] /= 2
        elif splt[0] == "tpl":
            registers[splt[1]] *= 3
        elif splt[0] == "inc":
            registers[splt[1]] += 1
        elif splt[0] == "jmp":
            pos += int(splt[1])
            continue
        elif splt[0] == "jie":
            if registers[splt[1].strip(",")] % 2 == 0:
                pos += int(splt[2])
                continue
        elif splt[0] == "jio":
            if registers[splt[1].strip(",")] == 1:
                pos += int(splt[2])
                continue

        pos += 1

    return registers


def part_one(inpt: list[str]) -> dict:
    registers = {"a": 0, "b": 0}
    return process(inpt, registers)


def part_two(inpt: list[str]) -> dict:
    registers = {"a": 1, "b": 0}
    return process(inpt, registers)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f'Example: {part_one(inpt=input_string)["a"]}')

    input_string = get_input(filename="input")
    print(f'Part one: {part_one(inpt=input_string)["b"]}')
    print(f'Part two: {part_two(inpt=input_string)["b"]}')
