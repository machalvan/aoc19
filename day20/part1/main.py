from utils import read_input, write_output, check_result
import re


def calc(lines):
    result = ''
    values = [line.strip('\n') for line in lines]
    print(values)
    portals = {}
    labels = {}

    x, y = 0, 0

    for y in range(0, len(values)):
        for x in range(0, len(values[0])):
            char = values[y][x]

            if char == ' ':
                continue

            if char == '.':
                pass

            if char == '#':
                pass

            if y < 2:
                labels[(x, 2)] = labels[(x, 2)] + char if (x, 2) in labels else char

    print(labels)
    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
