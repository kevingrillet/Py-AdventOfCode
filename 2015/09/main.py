import itertools
import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def process(inpt: list[str]) -> tuple[int, int]:
    regex_distances = re.compile(r"(\w*) to (\w*) = (\d*)")
    routes = inpt.copy()
    places = set()

    for route in routes:
        place_start, place_destination, distance = map(str, regex_distances.findall(route)[0])
        places.add(place_start)
        places.add(place_destination)

    permutations = list(itertools.permutations(places))

    shortest = 10000
    longest = 0

    for permutation in permutations:
        distance = 0
        step = 0
        while step < len(permutation) - 1:
            place_start = permutation[step]
            place_destination = permutation[step + 1]

            regex_from_to = re.compile(r"{} to {} = (\d*)".format(place_start, place_destination))
            regex_to_from = re.compile(r"{} to {} = (\d*)".format(place_destination, place_start))

            for route in routes:
                if regex_from_to.search(route):
                    distance += int(regex_from_to.search(route).group(1))
                    break
                elif regex_to_from.search(route):
                    distance += int(regex_to_from.search(route).group(1))
                    break

            step += 1

        if distance < shortest:
            shortest = distance
        if distance > longest:
            longest = distance

    return shortest, longest


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {process(inpt=input_string)}")

    input_string = get_input(filename="input")
    output = process(inpt=input_string)
    print(f"Part one: {output[0]}")
    print(f"Part two: {output[1]}")
