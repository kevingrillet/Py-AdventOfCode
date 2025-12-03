import hashlib

# Number of leading zeroes required in MD5 hash
MD5_PREFIX_PART_ONE = "00000"  # Five zeroes
MD5_PREFIX_PART_TWO = "000000"  # Six zeroes


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def part_one(inpt: str) -> int:
    result = 0
    while True:
        hexa = hashlib.md5("{}{}".format(inpt, result).encode("utf8")).hexdigest()
        if str(hexa)[:5] == MD5_PREFIX_PART_ONE:
            return result
        result += 1


def part_two(inpt: str) -> int:
    result = 0
    while True:
        hexa = hashlib.md5("{}{}".format(inpt, result).encode("utf8")).hexdigest()
        if str(hexa)[:6] == MD5_PREFIX_PART_TWO:
            return result
        result += 1


if __name__ == "__main__":
    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
