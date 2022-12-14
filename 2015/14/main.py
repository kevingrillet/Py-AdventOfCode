import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str], duration: int) -> int:
    regex = re.compile(r'\w* can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.')
    result = 0

    for rein in inpt:
        speed, running_duration, rest_duration = map(int, regex.search(rein).groups())

        distance = 0
        elapsed = 0
        time = 0
        while time < duration:
            time += 1
            elapsed += 1
            distance += speed
            if elapsed == running_duration:
                elapsed = 0
                time += rest_duration

        if distance > result:
            result = distance

    return result


def part_two(inpt: list[str], duration: int) -> int:
    regex = re.compile(r'(\w*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.')
    reindeers = {}
    track = []

    for rein in inpt:
        name, speed, running_duration, rest_duration = map(str, regex.search(rein).groups())

        reindeers[name] = 0

        distance = 0
        running = True
        elapsed = 0
        splits = [name]
        time = 0
        while time < duration:
            time += 1
            elapsed += 1
            if running:
                distance += int(speed)
                if elapsed == int(running_duration):
                    running = False
                    elapsed = 0
            else:
                if elapsed == int(rest_duration):
                    running = True
                    elapsed = 0
            splits.append(distance)
        track.append(splits)

    for second in range(1, duration + 1):
        furthest = 0
        leader = ''
        for reindeer in track:
            if reindeer[second] > furthest:
                furthest = reindeer[second]
                leader = reindeer[0]
        reindeers[leader] += 1

    return max(reindeers.values())


if __name__ == '__main__':
    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string, duration=2503)}')
    print(f'Part two: {part_two(inpt=input_string, duration=2503)}')
