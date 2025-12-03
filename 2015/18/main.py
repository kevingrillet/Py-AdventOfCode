import numpy as np


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


adjacent_matrice = [
    [-1, -1],
    [0, -1],
    [1, -1],
    [-1, 0],
    [1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
]


def print_lights(lights: np.ndarray) -> None:
    for x in lights:
        print("".join(x))


def part_one(inpt: list[str], final_step: int = 100) -> int:
    lights = np.full((len(inpt), len(inpt)), ".", str)

    for x, line in enumerate(inpt):
        for y, light in enumerate(line):
            lights[x][y] = light

    step = 0
    while step < final_step:
        step += 1
        new_lights = np.full((len(inpt), len(inpt)), ".", str)

        for x in range(len(lights)):
            for y in range(len(lights)):

                neighbors_on = 0
                for neighbor in adjacent_matrice:
                    if (
                        x + neighbor[0] < 0
                        or x + neighbor[0] > len(lights) - 1
                        or y + neighbor[1] < 0
                        or y + neighbor[1] > len(lights) - 1
                    ):
                        continue
                    if lights[x + neighbor[0]][y + neighbor[1]] == "#":
                        neighbors_on += 1

                if lights[x][y] == "#" and neighbors_on in (2, 3):
                    new_lights[x][y] = "#"
                elif lights[x][y] != "#" and neighbors_on == 3:
                    new_lights[x][y] = "#"

        lights = new_lights
        # print(step)
        # print_lights(lights)

    return np.count_nonzero(lights == "#")


def part_two(inpt: list[str], final_step: int = 100) -> int:
    lights = np.full((len(inpt), len(inpt)), ".", str)
    corners = [
        [0, 0],
        [0, len(lights) - 1],
        [len(lights) - 1, 0],
        [len(lights) - 1, len(lights) - 1],
    ]

    for x, line in enumerate(inpt):
        for y, light in enumerate(line):
            lights[x][y] = light

    for corner in corners:
        lights[corner[0]][corner[1]] = "#"

    step = 0
    while step < final_step:
        step += 1
        new_lights = np.full((len(inpt), len(inpt)), ".", str)

        for x in range(len(lights)):
            for y in range(len(lights)):

                neighbors_on = 0
                for neighbor in adjacent_matrice:
                    if (
                        x + neighbor[0] < 0
                        or x + neighbor[0] > len(lights) - 1
                        or y + neighbor[1] < 0
                        or y + neighbor[1] > len(lights) - 1
                    ):
                        continue
                    if lights[x + neighbor[0]][y + neighbor[1]] == "#":
                        neighbors_on += 1

                if lights[x][y] == "#" and neighbors_on in (2, 3):
                    new_lights[x][y] = "#"
                elif lights[x][y] != "#" and neighbors_on == 3:
                    new_lights[x][y] = "#"

        for corner in corners:
            new_lights[corner[0]][corner[1]] = "#"

        lights = new_lights
        # print(step)
        # print_lights(lights)

    return np.count_nonzero(lights == "#")


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example one: {part_one(inpt=input_string, final_step=4)}")
    print(f"Example two: {part_two(inpt=input_string, final_step=5)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
