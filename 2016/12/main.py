from collections import defaultdict


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def parse_instructions(inpt: list[str]) -> list[tuple]:
    """Pre-parse all instructions to avoid repeated splits and isdigit checks."""
    parsed = []
    for line in inpt:
        parts = line.split()
        cmd = parts[0]
        if cmd == "cpy":
            # (cmd, source_value_or_register, is_value, target_register)
            src = parts[1]
            is_val = src.lstrip("-").isdigit()
            parsed.append((cmd, int(src) if is_val else src, is_val, parts[2]))
        elif cmd in ("inc", "dec"):
            # (cmd, register)
            parsed.append((cmd, parts[1]))
        elif cmd == "jnz":
            # (cmd, test_value_or_register, is_value, offset)
            test = parts[1]
            is_val = test.lstrip("-").isdigit()
            parsed.append((cmd, int(test) if is_val else test, is_val, int(parts[2])))
    return parsed


def execute(parsed: list[tuple], initial_c: int = 0) -> int:
    """Execute parsed instructions with given initial value for register c."""
    registers = defaultdict(int)
    registers["c"] = initial_c
    index = 0

    while index < len(parsed):
        instruction = parsed[index]
        cmd = instruction[0]

        if cmd == "cpy":
            _, src, is_val, target = instruction
            registers[target] = src if is_val else registers[src]
        elif cmd == "inc":
            registers[instruction[1]] += 1
        elif cmd == "dec":
            registers[instruction[1]] -= 1
        elif cmd == "jnz":
            _, test, is_val, offset = instruction
            test_val = test if is_val else registers[test]
            if test_val != 0:
                index += offset
                continue
        index += 1

    return registers["a"]


def part_one(inpt: list[str]) -> int:
    parsed = parse_instructions(inpt)
    return execute(parsed, initial_c=0)


def part_two(inpt: list[str]) -> int:
    parsed = parse_instructions(inpt)
    return execute(parsed, initial_c=1)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
