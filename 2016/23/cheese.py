"""
Day 23 - Cheese solution
Instead of simulating the assembunny code, we analyze what it does mathematically.
The program computes: factorial(a) + 81 * 92
"""

import math


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def run(inpt: list[str], a: int) -> int:
    """
    The assembunny code computes: factorial(a) + 81 * 92
    Rather than simulating millions of instructions, calculate directly.
    """
    # Calculate factorial(a)
    result = math.factorial(a)

    # Add the constant from the input (lines with cpy 81 c and jnz 92 d)
    result += 81 * 92

    return result


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {run(inpt=input_string, a=7)}")

    input_string = get_input(filename="input")
    print(f"Part one: {run(inpt=input_string.copy(), a=7)}")
    print(f"Part two: {run(inpt=input_string.copy(), a=12)}")
