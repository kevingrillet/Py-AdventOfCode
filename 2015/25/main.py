import re

# Code generation parameters
STARTING_CODE = 20151125
CODE_MULTIPLIER = 252533
CODE_MODULO = 33554393


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def get_code_at_position(row: int, col: int) -> int:
    """Calculate the code at given row and column."""
    # Calculate which iteration this position is at
    # Position in diagonal: sum of first (row+col-1) numbers, minus (row-1)
    diagonal = row + col - 1
    position = diagonal * (diagonal - 1) // 2 + col

    # Calculate code value
    code = STARTING_CODE
    for _ in range(position - 1):
        code = (code * CODE_MULTIPLIER) % CODE_MODULO

    return code


def part_one(row: int, col: int) -> int:
    return get_code_at_position(row, col)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    row, col = map(int, re.findall(r"\d+", input_string))
    print(f"Part one: {part_one(row, col)}")
