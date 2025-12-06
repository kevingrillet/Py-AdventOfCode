import hashlib

# Number of leading zeroes required in MD5 hash
MD5_PREFIX_PART_ONE = "00000"  # Five zeroes
MD5_PREFIX_PART_TWO = "000000"  # Six zeroes


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def find_hash_with_prefix(inpt: str, prefix: str) -> int:
    """Find the lowest number that produces an MD5 hash starting with the given prefix."""
    result = 0
    while True:
        hexa = hashlib.md5(f"{inpt}{result}".encode()).hexdigest()
        if hexa.startswith(prefix):
            return result
        result += 1


def part_one(inpt: str) -> int:
    return find_hash_with_prefix(inpt, MD5_PREFIX_PART_ONE)


def part_two(inpt: str) -> int:
    return find_hash_with_prefix(inpt, MD5_PREFIX_PART_TWO)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
