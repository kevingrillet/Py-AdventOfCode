import json
import re
from typing import Any


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    return sum(map(int, re.findall(r"-?\d+", inpt)))


def part_two(inpt: str) -> int:
    json_input = json.loads(inpt)

    def process(item: Any) -> int:
        if isinstance(item, str):
            return 0
        if isinstance(item, int):
            return item
        if isinstance(item, list):
            return sum(process(subitem) for subitem in item)
        if isinstance(item, dict):
            if "red" in item.values():
                return 0
            return process(list(item.values()))
        raise ValueError(f"Unknown type: {type(item)}")

    return process(json_input)


if __name__ == "__main__":
    input_string = get_input(filename="input")

    # FML comments
    regex_comment = re.compile(r"//.*\n")
    input_string = regex_comment.sub("", input_string)

    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
