from collections import defaultdict

INSTRUCTION_PARTS = 2
INSTRUCTION_PARTS_WITH_ARG = 3
NESTED_MUL_PATTERN_LENGTH = 6
SIMPLE_ADD_PATTERN_LENGTH = 3


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def get_value(registers: defaultdict, key: str) -> int:
    """Get register value or parse integer."""
    return registers[key] if key.isalpha() else int(key)


def process_inc(registers: defaultdict, splt: list[str]) -> None:
    """Process inc instruction."""
    registers[splt[1]] += 1


def process_dec(registers: defaultdict, splt: list[str]) -> None:
    """Process dec instruction."""
    registers[splt[1]] -= 1


def process_jnz(registers: defaultdict, splt: list[str], i: int) -> int:
    """Process jnz instruction. Returns new instruction pointer."""
    v1 = get_value(registers, splt[1])
    if v1 != 0:
        return i + get_value(registers, splt[2])
    return i + 1


def process_cpy(registers: defaultdict, splt: list[str], i: int) -> int:
    """Process cpy instruction. Returns new instruction pointer."""
    if splt[2].isnumeric():
        print(i, " ".join(splt))
        return i + 1
    registers[splt[2]] = get_value(registers, splt[1])
    return i + 1


def process_tgl(registers: defaultdict, splt: list[str], inpt: list[str], i: int) -> None:
    """Process tgl instruction."""
    ii = i + get_value(registers, splt[1])
    if 0 <= ii < len(inpt):
        tmp = inpt[ii].split()
        if len(tmp) == INSTRUCTION_PARTS:
            tmp[0] = "dec" if tmp[0] == "inc" else "inc"
        else:
            tmp[0] = "cpy" if tmp[0] == "jnz" else "jnz"
        inpt[ii] = " ".join(tmp)


def run(inpt: list[str], a: int) -> int:
    registers = defaultdict(int)
    registers["a"] = a
    i = 0

    while i < len(inpt):
        # Optimization 1: Detect nested multiplication pattern (a += b * d, c=0, d=0)
        # cpy b c / inc a / dec c / jnz c -2 / dec d / jnz d -5
        if i + NESTED_MUL_PATTERN_LENGTH < len(inpt):
            parts = [line.split() for line in inpt[i : i + NESTED_MUL_PATTERN_LENGTH]]
            if (
                len(parts) == NESTED_MUL_PATTERN_LENGTH
                and parts[0][0] == "cpy"
                and len(parts[0]) == INSTRUCTION_PARTS_WITH_ARG
                and parts[1][0] == "inc"
                and len(parts[1]) == INSTRUCTION_PARTS
                and parts[2][0] == "dec"
                and len(parts[2]) == INSTRUCTION_PARTS
                and parts[3][0] == "jnz"
                and len(parts[3]) == INSTRUCTION_PARTS_WITH_ARG
                and parts[3][2] == "-2"
                and parts[4][0] == "dec"
                and len(parts[4]) == INSTRUCTION_PARTS
                and parts[5][0] == "jnz"
                and len(parts[5]) == INSTRUCTION_PARTS_WITH_ARG
                and parts[5][2] == "-5"
                and parts[0][2] == parts[2][1] == parts[3][1]  # c register
                and parts[4][1] == parts[5][1]  # d register
            ):
                # Nested multiplication: a += b * d
                b_val = get_value(registers, parts[0][1])
                c_reg = parts[0][2]
                a_reg = parts[1][1]
                d_reg = parts[4][1]
                registers[a_reg] += b_val * registers[d_reg]
                registers[c_reg] = 0
                registers[d_reg] = 0
                i += NESTED_MUL_PATTERN_LENGTH
                continue

        # Optimization 2: Detect simple addition pattern (X += Y, Y = 0)
        # inc X / dec Y / jnz Y -2
        if i + SIMPLE_ADD_PATTERN_LENGTH < len(inpt):
            parts = [line.split() for line in inpt[i : i + SIMPLE_ADD_PATTERN_LENGTH]]
            if (
                len(parts[0]) == INSTRUCTION_PARTS
                and parts[0][0] == "inc"
                and len(parts[1]) == INSTRUCTION_PARTS
                and parts[1][0] == "dec"
                and len(parts[2]) == INSTRUCTION_PARTS_WITH_ARG
                and parts[2][0] == "jnz"
                and parts[2][1] == parts[1][1]
                and parts[2][2] == "-2"
            ):
                target_reg = parts[0][1]
                source_reg = parts[1][1]
                registers[target_reg] += registers[source_reg]
                registers[source_reg] = 0
                i += SIMPLE_ADD_PATTERN_LENGTH
                continue

        splt = inpt[i].split(" ")
        instruction = splt[0]

        if instruction == "inc":
            process_inc(registers, splt)
            i += 1
        elif instruction == "dec":
            process_dec(registers, splt)
            i += 1
        elif instruction == "jnz":
            i = process_jnz(registers, splt, i)
        elif instruction == "cpy":
            i = process_cpy(registers, splt, i)
        elif instruction == "tgl":
            process_tgl(registers, splt, inpt, i)
            i += 1
        else:
            i += 1

    return registers["a"]


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {run(inpt=input_string, a=7)}")

    input_string = get_input(filename="input")
    print(f"Part one: {run(inpt=input_string.copy(), a=7)}")
    print(f"Part two: {run(inpt=input_string.copy(), a=12)}")
