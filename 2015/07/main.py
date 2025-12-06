import re
from collections import deque

import numpy as np


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def get_value(wires: dict, key: str) -> int:
    """Get wire value or convert string number to int."""
    return int(key) if key.isdigit() else wires[key]


def apply_not(wires: dict, match) -> int:
    """Apply NOT operation."""
    return int(~np.uint16(get_value(wires, match.group(1))))


def apply_and(wires: dict, match) -> int:
    """Apply AND operation."""
    return get_value(wires, match.group(1)) & get_value(wires, match.group(2))


def apply_or(wires: dict, match) -> int:
    """Apply OR operation."""
    return get_value(wires, match.group(1)) | get_value(wires, match.group(2))


def apply_lshift(wires: dict, match) -> int:
    """Apply LSHIFT operation."""
    return get_value(wires, match.group(1)) << get_value(wires, match.group(2))


def apply_rshift(wires: dict, match) -> int:
    """Apply RSHIFT operation."""
    return get_value(wires, match.group(1)) >> get_value(wires, match.group(2))


def compute(wires: dict, ins: str) -> bool:
    """Process a single instruction. Returns True if successful."""
    parts = ins.split(" -> ")
    wire_target = parts[1]

    operations = {
        "NOT": (r"NOT (\w+)", apply_not),
        "AND": (r"(\w+) AND (\w+)", apply_and),
        "OR": (r"(\w+) OR (\w+)", apply_or),
        "LSHIFT": (r"(\w+) LSHIFT (\w+)", apply_lshift),
        "RSHIFT": (r"(\w+) RSHIFT (\w+)", apply_rshift),
    }

    try:
        for op_name, (pattern, op_func) in operations.items():
            if op_name in parts[0]:
                match = re.match(pattern, parts[0])
                if not match:
                    return False
                wires[wire_target] = int(op_func(wires, match))
                return True

        # Direct assignment
        wires[wire_target] = int(get_value(wires, parts[0]))
        return True
    except (KeyError, AttributeError):
        return False


def part_one(inpt: list[str]) -> dict:
    instructions = deque(inpt)
    wires = {}

    while instructions:
        instruction = instructions.popleft()
        if not compute(wires, instruction):
            instructions.append(instruction)  # Retry later

    return dict(sorted(wires.items()))


def part_two(inpt: list[str], input_wires: dict) -> dict:
    instructions = deque(inpt)
    wires = {"b": input_wires["a"]}

    while instructions:
        instruction = instructions.popleft()
        wire_target = instruction.split(" -> ")[1]
        if wire_target != "b" and not compute(wires, instruction):
            instructions.append(instruction)  # Retry later

    return dict(sorted(wires.items()))


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    wires_one = part_one(inpt=input_string)
    # print(f'Part one: {wires_one}')
    print(f'Part one: {wires_one["a"]}')
    wires_two = part_two(inpt=input_string, input_wires=wires_one)
    # print(f'Part two: {wires_two}')
    print(f'Part two: {wires_two["a"]}')
