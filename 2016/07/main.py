import re


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def abba(sup: str) -> bool:
    return any(a == d and b == c and a != b for a, b, c, d in zip(sup, sup[1:], sup[2:], sup[3:]))


def ababab(sup: str, hyp: str) -> bool:
    return any(a == c and a != b and b + a + b in hyp for a, b, c in zip(sup, sup[1:], sup[2:]))


def part_one(inpt: list[str]) -> int:
    lines = [re.split(r"\[|]", line) for line in inpt]
    supernet = [" ".join(line[::2]) for line in lines]
    hypernet = [" ".join(line[1::2]) for line in lines]
    return sum(abba(sup) and not abba(hyp) for sup, hyp in zip(supernet, hypernet))


def part_two(inpt: list[str]) -> int:
    lines = [re.split(r"\[|]", line) for line in inpt]
    supernet = [" ".join(line[::2]) for line in lines]
    hypernet = [" ".join(line[1::2]) for line in lines]
    return sum(ababab(sup, hyp) for sup, hyp in zip(supernet, hypernet))


if __name__ == "__main__":
    print("Example one:", part_one(inpt=get_input(filename="example")))
    print("Example two:", part_two(inpt=get_input(filename="example2")))

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
