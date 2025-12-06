import re

MIN_DOUBLE_PAIRS = 2


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def has_straight(password: str) -> bool:
    """Check if password has three consecutive increasing letters."""
    return any(
        ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2
        for i in range(len(password) - 2)
    )


def process(inpt: str) -> str:
    regex_mistaken = re.compile(r"[iol]")
    regex_double = re.compile(r"(.)\1")
    password_list = list(inpt)

    while True:
        # Increment password
        for i in range(len(password_list) - 1, -1, -1):
            if password_list[i] == "z":
                password_list[i] = "a"
            else:
                password_list[i] = chr(ord(password_list[i]) + 1)
                break

        password = "".join(password_list)

        if regex_mistaken.search(password) or len(regex_double.findall(password)) < MIN_DOUBLE_PAIRS:
            continue

        if has_straight(password):
            return password


if __name__ == "__main__":
    input_string = get_input(filename="input")
    output_one = process(inpt=input_string)
    print(f"Part one: {output_one}")
    print(f"Part two: {process(inpt=output_one)}")
