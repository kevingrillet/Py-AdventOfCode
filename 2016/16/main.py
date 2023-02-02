def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def run(inpt: str, fill: int) -> str:
    # Fill
    data = inpt
    while len(data) < fill:
        tmp = data + '0'
        for c in data[::-1]:
            if c == '1':
                tmp += '0'
            else:
                tmp += '1'
        data = tmp
    data = data[:fill]

    # Checksum
    while len(data) % 2 == 0:
        tmp = ''
        i = 0
        while i < len(data) - 1:
            if data[i] == data[i + 1]:
                tmp += '1'
            else:
                tmp += '0'
            i += 2
        data = tmp

    return data


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {run(inpt=input_string, fill=20)}')

    input_string = get_input(filename='input')
    print(f'Part one: {run(inpt=input_string, fill=272)}')
    print(f'Part two: {run(inpt=input_string, fill=35651584)}')
