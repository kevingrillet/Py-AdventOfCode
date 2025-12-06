import numpy as np

MIN_NEIGHBORS_TO_SPAWN = 3
MIN_NEIGHBORS_TO_SURVIVE = 2
MAX_NEIGHBORS_TO_SURVIVE = 3


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def simulate_lights(inpt: list[str], final_step: int, stuck_corners: bool = False) -> int:
    """Simulate Conway's Game of Life for lights using optimized numpy."""
    size = len(inpt)
    # Use integers instead of strings: 1 for on, 0 for off
    lights = np.array([[1 if c == "#" else 0 for c in line] for line in inpt], dtype=np.uint8)

    if stuck_corners:
        lights[0, 0] = lights[0, size - 1] = lights[size - 1, 0] = lights[size - 1, size - 1] = 1

    for _ in range(final_step):
        # Use scipy-like convolution approach for counting neighbors
        # Pad the array with zeros
        padded = np.pad(lights, 1, mode="constant", constant_values=0)

        # Count neighbors using array slicing
        neighbors = (
            padded[:-2, :-2]  # top-left
            + padded[:-2, 1:-1]  # top
            + padded[:-2, 2:]  # top-right
            + padded[1:-1, :-2]  # left
            + padded[1:-1, 2:]  # right
            + padded[2:, :-2]  # bottom-left
            + padded[2:, 1:-1]  # bottom
            + padded[2:, 2:]  # bottom-right
        )

        # Apply Game of Life rules
        # A light stays on if it has 2 or 3 neighbors on
        # A light turns on if it has exactly 3 neighbors on
        lights = (
            (lights == 1) & ((neighbors == MIN_NEIGHBORS_TO_SURVIVE) | (neighbors == MAX_NEIGHBORS_TO_SURVIVE))
        ) | ((lights == 0) & (neighbors == MIN_NEIGHBORS_TO_SPAWN))
        lights = lights.astype(np.uint8)

        if stuck_corners:
            lights[0, 0] = lights[0, size - 1] = lights[size - 1, 0] = lights[size - 1, size - 1] = 1

    return int(np.sum(lights))


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
