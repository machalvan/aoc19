from utils import read_input, write_output, check_result
import re


def calc(lines):
    pointer = 0
    parser = re.compile("-?\d+")
    words = [int(x) for line in lines for x in parser.findall(line.strip())]

    words[1] = 12
    words[2] = 2

    while pointer < len(words):
        opcode = int(words[pointer])
        if opcode == 1:
            pointer += 1
            index = int(words[pointer])
            value1 = int(words[index])

            pointer += 1
            index = int(words[pointer])
            value2 = int(words[index])

            sum = value1 + value2
            pointer += 1
            index = int(words[pointer])
            words[index] = sum

        elif opcode == 2:
            pointer += 1
            index = int(words[pointer])
            value1 = int(words[index])

            pointer += 1
            index = int(words[pointer])
            value2 = int(words[index])

            sum = value1 * value2
            pointer += 1
            index = int(words[pointer])
            words[index] = sum

        elif opcode == 99:
            break

        pointer += 1

    result = words[0]
    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
