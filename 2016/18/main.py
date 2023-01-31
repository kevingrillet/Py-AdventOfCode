def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


def run(inpt: str, max_row: int) -> int:
    row = inpt
    safe = 0
    for i in range(max_row):
        safe += row.count('.')
        old = '.' + row + '.'
        row = ''
        for x in range(len(old)-2):
            row += '^' if old[x] != old[x+2] else '.'
    return safe


if __name__ == '__main__':
    input_string = get_input(filename='example')
    print(f'Example: {run(inpt=input_string, max_row=3)}')
    input_string = get_input(filename='example2')
    print(f'Example: {run(inpt=input_string, max_row=10)}')

    input_string = get_input(filename='input')
    print(f'Part one: {run(inpt=input_string, max_row=40)}')
    print(f'Part two: {run(inpt=input_string, max_row=400000)}')
