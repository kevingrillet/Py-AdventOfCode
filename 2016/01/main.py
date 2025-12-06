def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return f.read().strip().split(", ")


def part_one(inpt: list[str]) -> int:
    pos = [0, 0]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    for instruction in inpt:
        if instruction[0] == "R":
            direction = (direction + 1) % len(directions)
        else:
            direction = (direction - 1) % len(directions)

        steps = int(instruction[1:])
        pos = [pos[0] + directions[direction][0] * steps, pos[1] + directions[direction][1] * steps]

    return sum(map(abs, pos))


def part_two(inpt: list[str]) -> int:
    pos = [0, 0]
    visited = [[0, 0]]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = 0
    for instruction in inpt:
        if instruction[0] == "R":
            direction = (direction + 1) % len(directions)
        else:
            direction = (direction - 1) % len(directions)

        for _ in range(int(instruction[1:])):
            pos = [pos[0] + directions[direction][0], pos[1] + directions[direction][1]]
            if pos in visited:
                return sum(map(abs, pos))
            else:
                visited.append(pos)

    return sum(map(abs, pos))


if __name__ == "__main__":
    print("Example one:", {part_one(inpt=get_input(filename="example"))})
    print("Example two:", {part_one(inpt=get_input(filename="example2"))})
    print("Example three:", {part_one(inpt=get_input(filename="example3"))})

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")

    print("Example four:", {part_two(inpt=get_input(filename="example4"))})
    print(f"Part two: {part_two(inpt=input_string)}")
