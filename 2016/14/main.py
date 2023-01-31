from hashlib import md5


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    keys = set()
    triplets = {}
    index = 0

    while len(keys) < 64 or index < max(keys) + 1000:
        hex_value = md5((inpt + str(index)).encode()).hexdigest()
        found = False
        for a, b, c in zip(hex_value, hex_value[1:], hex_value[2:]):
            if a == b == c:
                if 5*a in hex_value:
                    for key, value in triplets.items():
                        if a == value and key < index <= key + 1000:
                            keys.add(key)
                if not found:
                    triplets[index] = a
                    found = True

        index += 1

    return sorted(keys)[63]


def part_two(inpt: str) -> int:
    keys = set()
    triplets = {}
    index = 0

    while len(keys) < 64 or index < max(keys) + 1000:
        hex_value = md5((inpt + str(index)).encode()).hexdigest()
        for _ in range(2016):
            hex_value = md5(hex_value.encode()).hexdigest()
        found = False
        for a, b, c in zip(hex_value, hex_value[1:], hex_value[2:]):
            if a == b == c:
                if 5*a in hex_value:
                    for key, value in triplets.items():
                        if a == value and key < index <= key + 1000:
                            keys.add(key)
                if not found:
                    triplets[index] = a
                    found = True

        index += 1

    return sorted(keys)[63]


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {part_one(inpt=input_string)}')

    input_string = get_input(filename='input')
    print(f'Part one: {part_one(inpt=input_string)}')
    print(f'Part two: {part_two(inpt=input_string)}')
