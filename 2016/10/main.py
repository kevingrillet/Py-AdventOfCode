from collections import defaultdict
from typing import Optional

TARGET_LOW_VALUE = 17
TARGET_HIGH_VALUE = 61


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def _add_to_bot(bots: defaultdict, bot: str, value: int, todos: list[str]) -> None:
    bots[bot].append(value)
    if len(bots[bot]) > 1:
        todos.append(bot)


def _send_to(
    link: list[str], bots: defaultdict, value: int, todos: list[str], output: Optional[defaultdict] = None
) -> None:
    if link[0] == "bot":
        _add_to_bot(bots, link[1], value, todos)
    elif output is not None:
        output[link[1]].append(value)


def part_one(inpt: list[str]) -> str:
    result: Optional[str] = None
    init = [line.split(" ") for line in inpt if line.startswith("value")]
    cmd = [line.split(" ") for line in inpt if not line.startswith("value")]

    bots = defaultdict(list)
    todos = []
    for line in init:
        _add_to_bot(bots, line[-1], int(line[1]), todos)

    links = {}
    for line in cmd:
        links[line[1]] = (line[5:7], line[-2:])

    while todos:
        bot = todos.pop()
        low_v, high_v = sorted(bots[bot])
        if low_v == TARGET_LOW_VALUE and high_v == TARGET_HIGH_VALUE:
            result = bot
            break
        low_l, high_l = links[bot]
        _send_to(low_l, bots, low_v, todos)
        _send_to(high_l, bots, high_v, todos)

    return result if result is not None else ""


def part_two(inpt: list[str]) -> int:
    init = [line.split(" ") for line in inpt if line.startswith("value")]
    cmd = [line.split(" ") for line in inpt if not line.startswith("value")]

    bots = defaultdict(list)
    todos = []
    for line in init:
        _add_to_bot(bots, line[-1], int(line[1]), todos)

    links = {}
    for line in cmd:
        links[line[1]] = (line[5:7], line[-2:])

    output = defaultdict(list)
    while todos:
        bot = todos.pop()
        low_v, high_v = sorted(bots[bot])
        low_l, high_l = links[bot]
        _send_to(low_l, bots, low_v, todos, output=output)
        _send_to(high_l, bots, high_v, todos, output=output)

    return output["0"][0] * output["1"][0] * output["2"][0]


if __name__ == "__main__":
    # input_string = get_input(filename='example')
    # print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
