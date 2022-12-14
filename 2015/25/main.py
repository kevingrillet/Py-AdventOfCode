import re


def get_input(filename: str) -> str:
    with open(filename, encoding="utf8") as f:
        return f.read().strip()


dest_row = 0
dest_col = 0


def process(code: int) -> int:
    row = col = 1
    while True:
        code = (code * 252533) % 33554393
        if row == 1:
            row = col + 1
            col = 1

        else:
            row -= 1
            col += 1

        if dest_row == row and dest_col == col:
            return code


if __name__ == '__main__':
    input_string = get_input(filename='input')
    regex = re.compile(r'row (\d+), column (\d+).')

    dest_row, dest_col = map(int, regex.search(input_string).groups())

    print(f'Part one: {process(20151125)}')
