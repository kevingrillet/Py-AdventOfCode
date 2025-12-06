def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def run(inpt: str, fill: int) -> str:
    # Fill - use list for efficiency
    data = list(inpt)
    while len(data) < fill:
        # Create reversed copy with flipped bits
        reversed_flipped = ["0" if c == "1" else "1" for c in reversed(data)]
        data.extend(["0"])
        data.extend(reversed_flipped)

    # Truncate to desired length
    data = data[:fill]

    # Checksum - keep reducing while even length
    while len(data) % 2 == 0:
        new_data = []
        for i in range(0, len(data), 2):
            new_data.append("1" if data[i] == data[i + 1] else "0")
        data = new_data

    return "".join(data)


if __name__ == "__main__":
    input_string = get_input(filename="example")
    print(f"Example: {run(inpt=input_string, fill=20)}")

    input_string = get_input(filename="input")
    print(f"Part one: {run(inpt=input_string, fill=272)}")
    print(f"Part two: {run(inpt=input_string, fill=35651584)}")
