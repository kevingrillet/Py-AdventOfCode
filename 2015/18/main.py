import numpy as np

MIN_NEIGHBORS_TO_SPAWN = 3


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


ADJACENT_OFFSETS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def count_neighbors(lights: np.ndarray, x: int, y: int, size: int) -> int:
    """Count lit neighbors for a given position."""
    count = 0
    for dx, dy in ADJACENT_OFFSETS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and lights[nx][ny] == "#":
            count += 1
    return count


def simulate_lights(inpt: list[str], final_step: int, stuck_corners: bool = False) -> int:
    """Simulate Conway's Game of Life for lights."""
    size = len(inpt)
    lights = np.array([list(line) for line in inpt])

    corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)] if stuck_corners else []

    for corner in corners:
        lights[corner] = "#"

    for _ in range(final_step):
        new_lights = np.full((size, size), ".", str)

        for x in range(size):
            for y in range(size):
                neighbors_on = count_neighbors(lights, x, y, size)

                if lights[x][y] == "#" and neighbors_on in (2, MIN_NEIGHBORS_TO_SPAWN):
                    new_lights[x][y] = "#"
                elif lights[x][y] == "." and neighbors_on == MIN_NEIGHBORS_TO_SPAWN:
                    new_lights[x][y] = "#"

        for corner in corners:
            new_lights[corner] = "#"

        lights = new_lights

    return np.count_nonzero(lights == "#")


def part_one(inpt: list[str], final_step: int = 100) -> int:
    return simulate_lights(inpt, final_step, stuck_corners=False)


def part_two(inpt: list[str], final_step: int = 100) -> int:
    return simulate_lights(inpt, final_step, stuck_corners=True)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example one: {part_one(inpt=input_string, final_step=4)}")
    print(f"Example two: {part_two(inpt=input_string, final_step=5)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
