from collections import defaultdict

MIN_SIGNAL_LENGTH = 10


def get_input(filename: str) -> list[str]:
    with open(filename, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


def run(inpt: list[str], a: int) -> int:
    registers = defaultdict(int)
    registers["a"] = a
    signals = [1]
    i = 0

    while i < len(inpt):
        # print(i, inpt[i], registers)
        splt = inpt[i].split(" ")
        if splt[0] == "inc":
            registers[splt[1]] += 1
        elif splt[0] == "dec":
            registers[splt[1]] -= 1
        elif splt[0] == "jnz":
            v1 = registers[splt[1]] if splt[1].isalpha() else int(splt[1])
            if v1 != 0:
                i += registers[splt[2]] if splt[2].isalpha() else int(splt[2])
                continue
        elif splt[0] == "cpy":
            if splt[1].isalpha():
                registers[splt[2]] = registers[splt[1]]
            else:
                registers[splt[2]] = int(splt[1])
        elif splt[0] == "out":
            x = registers[splt[1]] if splt[1].isalpha() else int(splt[1])
            if x not in {0, 1} or x == signals[-1]:
                return False
            else:
                signals.append(x)
            if len(signals) > MIN_SIGNAL_LENGTH:
                return True
        i += 1
    return registers["a"]


if __name__ == "__main__":
    input_string = get_input(filename="input")

    z = 0
    while not run(inpt=input_string.copy(), a=z):
        z += 1

    print(f"Part one: {z}")
