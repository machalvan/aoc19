from utils import read_input, write_output, check_result
import re


def calc(lines):
    parser = re.compile("-?\d+")
    values = [[int(char) for char in line] for line in lines][0]
    w = 25
    h = 6

    print(values)
    layers = [values[x:x + w*h] for x in range(0, len(values), w*h)]
    print(layers)

    zero_layer = []
    zeros = 9999
    for layer in layers:
        if layer.count(0) < zeros:
            zeros = layer.count(0)
            zero_layer = layer

    return zero_layer.count(1) * zero_layer.count(2)


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)