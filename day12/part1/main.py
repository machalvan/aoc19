from utils import read_input, write_output, check_result
import re


def calc(lines):
    parser = re.compile("-?\d+")
    values = [[int(i) for i in parser.findall(line.strip())] for line in lines]
    steps = 1000

    for value in values:
        value.extend([0,0,0])

    for step in range(1, steps + 1):
        for i, moon in enumerate(values):
            for i2, moon2 in enumerate(values):
                if i == i2:
                    continue

                for j in range(0, 3):
                    moon[3 + j] += 1 if moon[j] < moon2[j] else (0 if moon2[j] == moon[j] else -1)

        for moon in values:
            for j in range(0, 3):
                moon[j] += moon[3 + j]

    for value in values:
        value.extend([0,0])

    totals = []
    for moon in values:
        moon[6] = sum(abs(moon[i]) for i in [0,1,2])
        moon[7] = sum(abs(moon[i]) for i in [3,4,5])
        totals.append(moon[6] * moon[7])

    return sum(totals)


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
