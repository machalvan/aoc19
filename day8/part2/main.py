from utils import read_input, write_output, check_result
import re


def calc(lines):
    parser = re.compile("-?\d+")
    values = [[int(char) for char in line] for line in lines][0]
    w = 25
    h = 6
    area = w*h

    layers = [values[x:x + area] for x in range(0, len(values), area)]

    image = [-1] * area
    for layer in layers:
        for i in range(0, area):
            d = layer[i]
            if d != 2 and image[i] == -1:
                image[i] = d

    msg = ''
    for i in range(0, area):
        msg += str(image[i])
        if (i + 1) % w == 0:
            msg += '\n'

    msg = msg.replace('0', ' ')
    msg = msg.replace('1', '#')
    return msg


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)