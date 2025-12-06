import re
from dataclasses import dataclass

# Race duration in seconds
RACE_DURATION = 2503


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


@dataclass
class Reindeer:
    name: str
    speed: int
    run_time: int
    rest_time: int

    def distance_at_time(self, time: int) -> int:
        """Calculate distance traveled at given time."""
        cycle_time = self.run_time + self.rest_time
        full_cycles = time // cycle_time
        remaining_time = time % cycle_time

        distance = full_cycles * self.speed * self.run_time
        distance += min(remaining_time, self.run_time) * self.speed
        return distance


def parse_reindeers(inpt: list[str]) -> list[Reindeer]:
    """Parse input into list of Reindeer objects."""
    regex = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
    reindeers = []
    for line in inpt:
        match = regex.search(line)
        if not match:
            continue
        name, speed, run_time, rest_time = match.groups()
        reindeers.append(Reindeer(name, int(speed), int(run_time), int(rest_time)))
    return reindeers


def part_one(inpt: list[str], duration: int) -> int:
    reindeers = parse_reindeers(inpt)
    return max(r.distance_at_time(duration) for r in reindeers)


def part_two(inpt: list[str], duration: int) -> int:
    reindeers = parse_reindeers(inpt)
    points = {r.name: 0 for r in reindeers}

    for second in range(1, duration + 1):
        distances = {r.name: r.distance_at_time(second) for r in reindeers}
        max_distance = max(distances.values())
        for name, distance in distances.items():
            if distance == max_distance:
                points[name] += 1

    return max(points.values())


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string, duration=RACE_DURATION)}")
    print(f"Part two: {part_two(inpt=input_string, duration=RACE_DURATION)}")
