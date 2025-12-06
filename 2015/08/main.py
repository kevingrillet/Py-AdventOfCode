import ast


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    """Calculate difference between code and memory representation."""
    result = 0
    for line in inpt:
        code_length = len(line)
        memory_length = len(ast.literal_eval(line))
        result += code_length - memory_length
    return result


def part_two(inpt: list[str]) -> int:
    """Calculate difference between encoded and original representation."""
    result = 0
    for line in inpt:
        original_length = len(line)
        # Encode: add outer quotes and escape internal quotes and backslashes
        encoded_length = len(line.replace("\\", "\\\\").replace('"', '\\"')) + 2
        result += encoded_length - original_length
    return result


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
