from hashlib import md5

KEYS_NEEDED = 64


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def get_hash(input_base: str, index: int, stretch: int) -> str:
    """Generate hash with optional key stretching."""
    hash_hex = md5((input_base + str(index)).encode()).hexdigest()
    for _ in range(stretch):
        hash_hex = md5(hash_hex.encode()).hexdigest()
    return hash_hex


def find_keys(inpt: str, stretch: int = 0) -> int:
    """Find the 64th key index with optional key stretching."""
    keys = set()
    triplets = {}
    index = 0

    while len(keys) < KEYS_NEEDED or index < max(keys) + 1000:
        hex_value = get_hash(inpt, index, stretch)
        found = False

        for a, b, c in zip(hex_value, hex_value[1:], hex_value[2:]):
            if a == b == c:
                if 5 * a in hex_value:
                    for key, value in triplets.items():
                        if a == value and key < index <= key + 1000:
                            keys.add(key)
                if not found:
                    triplets[index] = a
                    found = True

        index += 1

    return sorted(keys)[63]


def part_one(inpt: str) -> int:
    return find_keys(inpt, stretch=0)


def part_two(inpt: str) -> int:
    return find_keys(inpt, stretch=2016)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
