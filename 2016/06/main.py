def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def part_one(inpt: list[str]) -> str:
    result = ""
    for record in list(zip(*inpt)):
        frequency = {letter: record.count(letter) for letter in set(record)}
        sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        result += sorted_frequency[0][0]
    return result


def part_two(inpt: list[str]) -> str:
    result = ""
    for record in list(zip(*inpt)):
        frequency = {letter: record.count(letter) for letter in set(record)}
        sorted_frequency = sorted(frequency.items(), key=lambda x: (x[1], x[0]))
        result += sorted_frequency[0][0]
    return result


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example one: {part_one(inpt=input_string)}")
    print(f"Example two: {part_two(inpt=input_string)}")

    input_string = get_input(filename="input")
    print(f"Part one: {part_one(inpt=input_string)}")
    print(f"Part two: {part_two(inpt=input_string)}")
