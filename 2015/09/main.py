import itertools
import re
from collections import defaultdict


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: list[str]) -> tuple[int, int]:
    regex_distances = re.compile(r"(\w+) to (\w+) = (\d+)")
    distances = defaultdict(dict)
    places = set()

    # Build distance dictionary
    for route in inpt:
        match = regex_distances.search(route)
        if not match:
            continue
        place_start, place_destination, distance = match.groups()
        distance = int(distance)
        places.add(place_start)
        places.add(place_destination)
        distances[place_start][place_destination] = distance
        distances[place_destination][place_start] = distance

    # Calculate all route distances
    route_lengths = []
    for permutation in itertools.permutations(places):
        total_distance = sum(distances[permutation[i]][permutation[i + 1]] for i in range(len(permutation) - 1))
        route_lengths.append(total_distance)

    return min(route_lengths), max(route_lengths)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {process(inpt=input_string)}")

    input_string = get_input(filename="input")
    output = process(inpt=input_string)
    print(f"Part one: {output[0]}")
    print(f"Part two: {output[1]}")
