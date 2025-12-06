def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


DIRECTIONS = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def part_one(inpt: str) -> int:
    visited = {(0, 0)}
    x, y = 0, 0

    for direction in inpt:
        dx, dy = DIRECTIONS[direction]
        x, y = x + dx, y + dy
        visited.add((x, y))

    return len(visited)


def part_two(inpt: str) -> int:
    visited = {(0, 0)}
    positions = [(0, 0), (0, 0)]  # [santa, robo-santa]

    for i, direction in enumerate(inpt):
        dx, dy = DIRECTIONS[direction]
        x, y = positions[i % 2]
        positions[i % 2] = (x + dx, y + dy)
        visited.add(positions[i % 2])

    return len(visited)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
