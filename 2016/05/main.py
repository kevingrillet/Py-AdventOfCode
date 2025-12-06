import hashlib

PASSWORD_LENGTH = 8


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def find_passwords(inpt: str) -> tuple[str, str]:
    """Find both passwords simultaneously to avoid redundant MD5 calculations."""
    input_bytes = inpt.encode()
    result_one = []
    result_two = [""] * PASSWORD_LENGTH
    found_two = 0
    cpt = 0

    while len(result_one) < PASSWORD_LENGTH or found_two < PASSWORD_LENGTH:
        hash_hex = hashlib.md5(input_bytes + str(cpt).encode()).hexdigest()
        if hash_hex.startswith("00000"):
            # Part one: just take the 6th character
            if len(result_one) < PASSWORD_LENGTH:
                result_one.append(hash_hex[5])

            # Part two: use 6th character as position, 7th as value
            if found_two < PASSWORD_LENGTH:
                pos = hash_hex[5]
                if pos.isnumeric():
                    pos_int = int(pos)
                    if pos_int < PASSWORD_LENGTH and result_two[pos_int] == "":
                        result_two[pos_int] = hash_hex[6]
                        found_two += 1
        cpt += 1

    return "".join(result_one), "".join(result_two)


def part_one(inpt: str) -> str:
    return find_passwords(inpt)[0]


def part_two(inpt: str) -> str:
    return find_passwords(inpt)[1]


if __name__ == "__main__":
    input_string = get_input(filename="example")
    ex_one, ex_two = find_passwords(input_string)
    print(f"Example one: {ex_one}")
    print(f"Example two: {ex_two}")

    input_string = get_input(filename="input")
    res_one, res_two = find_passwords(input_string)
    print(f"Part one: {res_one}")
    print(f"Part two: {res_two}")
