import re
import string


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def process(inpt: str) -> str:
    alphabet = string.ascii_lowercase
    regex_mistaken = re.compile(r"[iol]")
    regex_double = re.compile(r"(.)\1")
    password = inpt
    password_reversed = list(reversed(password))
    password_new = ""

    while True:
        for pos, char in enumerate(password_reversed):
            if char == "z":
                password_reversed[pos] = "a"
            else:
                password_reversed[pos] = alphabet[alphabet.find(char) + 1]
                password_new = "".join(password_reversed)[-1::-1]
                break

        if (
            regex_mistaken.search(password_new)
            or len(regex_double.findall(password_new)) < 2
        ):
            continue

        straight = False
        pos = 0
        while pos < len(password_new) - 2:
            if (
                password_new[pos] not in ("y", "z")
                and password_new[pos + 1]
                == alphabet[alphabet.find(password_new[pos]) + 1]
                and password_new[pos + 2]
                == alphabet[alphabet.find(password_new[pos]) + 2]
            ):
                straight = True
                break
            pos += 1

        if straight:
            break

    return password_new


if __name__ == "__main__":
    input_string = get_input(filename="input")
    output_one = process(inpt=input_string)
    print(f"Part one: {output_one}")
    print(f"Part two: {process(inpt=output_one)}")
