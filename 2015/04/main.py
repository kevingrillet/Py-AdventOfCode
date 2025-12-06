import hashlib

# Number of leading zeroes required in MD5 hash
MD5_PREFIX_PART_ONE = "00000"  # Five zeroes
MD5_PREFIX_PART_TWO = "000000"  # Six zeroes


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def find_hash_with_prefix(inpt: str, prefix: str, start: int = 0) -> int:
    """Find the lowest number that produces an MD5 hash starting with the given prefix."""
    result = start
    input_bytes = inpt.encode()

    while True:
        hash_hex = hashlib.md5(input_bytes + str(result).encode()).hexdigest()
        if hash_hex.startswith(prefix):
            return result
        result += 1


def part_one(inpt: str) -> int:
    return find_hash_with_prefix(inpt, MD5_PREFIX_PART_ONE)


def part_two(inpt: str, part_one_result: int) -> int:
    # Start searching from part_one result + 1
    return find_hash_with_prefix(inpt, MD5_PREFIX_PART_TWO, part_one_result + 1)


if __name__ == "__main__":
    input_string = get_input(filename="input")
    result_one = part_one(inpt=input_string)
    print(f"Part one: {result_one}")
    print(f"Part two: {part_two(inpt=input_string, part_one_result=result_one)}")
