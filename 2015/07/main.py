import re

import numpy as np


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


regex_provide = re.compile(r'(\w+) -> (\w+)')
regex_gates = re.compile(r'(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)')
regex_complement = re.compile(r'NOT (\w+) -> (\w+)')


def compute(wires: dict, ins: str):
    value = 0
    wire_target = ""

    if regex_complement.search(ins):
        wire_value, wire_target = map(str, regex_complement.findall(ins)[0])
        value = ~np.uint16(wires[wire_value])
    elif regex_gates.search(ins):
        a, operator, b, wire_target = map(str, regex_gates.findall(ins)[0])

        if not a.isnumeric():
            a = wires[a]

        if not b.isnumeric():
            b = wires[b]

        a = int(a)
        b = int(b)

        if operator == 'AND':
            value = a & b
        elif operator == 'OR':
            value = a | b
        elif operator == 'LSHIFT':
            value = a << b
        elif operator == 'RSHIFT':
            value = a >> b

    elif regex_provide.search(ins):
        signal, wire_target = map(str, regex_provide.findall(ins)[0])

        if signal.isnumeric():
            value = signal
        else:
            value = wires[signal]

    wires[wire_target] = value


def part_one(inpt: list[str]) -> dict:
    instructions = inpt.copy()
    wires = {}

    while instructions:
        for instruction in instructions:
            try:
                compute(wires=wires, ins=instruction)
                instructions.remove(instruction)
            except KeyError:
                continue

    return dict(sorted(wires.items()))


def part_two(inpt: list[str], input_wires: dict) -> dict:
    instructions = inpt.copy()
    regex_target = re.compile(r'-> (\w+)')
    wires = {'b': input_wires['a']}

    while instructions:
        for instruction in instructions:
            try:
                if regex_target.search(instruction).group(1) != 'b':
                    compute(wires=wires, ins=instruction)
                instructions.remove(instruction)
            except KeyError:
                continue

    # https://youtrack.jetbrains.com/issue/PY-51195/Incorrect-warning-raised-in-dict
    return dict(sorted(wires.items()))


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    wires_one = part_one(inpt=input_string)
    # print(f'Part one: {wires_one}')
    print(f'Part one: {wires_one["a"]}')
    wires_two = part_two(inpt=input_string, input_wires=wires_one)
    # print(f'Part two: {wires_two}')
    print(f'Part two: {wires_two["a"]}')
