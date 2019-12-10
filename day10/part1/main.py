from utils import read_input, write_output, check_result
import re


def calc(lines):
    result = ''
    values = [[char for char in line.split()[0]] for line in lines]

    for value in values:
        print(value)  # Code here
    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
