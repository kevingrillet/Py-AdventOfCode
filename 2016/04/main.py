import re
import string


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> int:
    regex = re.compile(r"([a-z-]+)(\d+)\[(\w+)]")
    regex_letters = re.compile(r"([a-z])")

    result = 0
    for room in inpt:
        letters, sectorid, checksum = regex.findall(room)[0]
        frequency = {letter: letters.count(letter) for letter in set(regex_letters.findall(letters))}
        sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        if "".join(freq[0] for freq in sorted_frequency).startswith(checksum):
            result += int(sectorid)

    return result


def caesar_cipher(sid: int) -> dict:
    alphabet = string.ascii_lowercase
    rotation = int(sid) % len(alphabet)
    return str.maketrans(alphabet + "-", alphabet[rotation:] + alphabet[:rotation] + " ")


def part_two(inpt: list[str]) -> int:
    regex = re.compile(r"([a-z-]+)(\d+)\[(\w+)]")
    regex_letters = re.compile(r"([a-z])")

    for room in inpt:
        letters, sectorid, checksum = regex.findall(room)[0]
        frequency = {letter: letters.count(letter) for letter in set(regex_letters.findall(letters))}
        sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        if "".join(freq[0] for freq in sorted_frequency).startswith(checksum):
            if "north" in letters.translate(caesar_cipher(sectorid)):
                return int(sectorid)

    return -1


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {part_one(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
