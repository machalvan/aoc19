from utils import read_input, write_output, check_result
import re


def get_value_at_pointer(pointer, values):
    pointer += 1
    value = int(values[pointer])
    return pointer, value


def write_position_mode(pointer, values, value):
    pointer, address = get_value_at_pointer(pointer, values)
    values[address] = value
    return pointer, values


def read_position_mode(pointer, values):
    pointer, address = get_value_at_pointer(pointer, values)
    value = int(values[address])
    return pointer, value


def read_immediate_mode(pointer, values):
    pointer, value = get_value_at_pointer(pointer, values)
    return pointer, value


def add_op(pointer, values, params):
    value1, value2 = 0, 0
    param3, param2, param1 = params

    if param1 == 0:
        pointer, value1 = read_position_mode(pointer, values)
    elif param1 == 1:
        pointer, value1 = read_immediate_mode(pointer, values)

    if param2 == 0:
        pointer, value2 = read_position_mode(pointer, values)
    elif param2 == 1:
        pointer, value2 = read_immediate_mode(pointer, values)

    sum = value1 + value2
    pointer, values = write_position_mode(pointer, values, sum)

    return pointer, values


def mult_op(pointer, values, params):
    value1, value2 = 0, 0
    param3, param2, param1 = params

    if param1 == 0:
        pointer, value1 = read_position_mode(pointer, values)
    elif param1 == 1:
        pointer, value1 = read_immediate_mode(pointer, values)

    if param2 == 0:
        pointer, value2 = read_position_mode(pointer, values)
    elif param2 == 1:
        pointer, value2 = read_immediate_mode(pointer, values)

    product = value1 * value2
    pointer, values = write_position_mode(pointer, values, product)

    return pointer, values


def input_op(pointer, values, params, input_value):
    pointer, values = write_position_mode(pointer, values, input_value)
    return pointer, values


def output_op(pointer, values, params):
    value = 0
    param = params[0]

    if param == 0:
        pointer, value = read_position_mode(pointer, values)
    elif param == 1:
        pointer, value = read_immediate_mode(pointer, values)

    return pointer, value


def calc(lines):
    result = ''
    pointer = 0
    parser = re.compile("-?\d+")
    values = [int(x) for line in lines for x in parser.findall(line.strip())]
    input_value = 1

    while pointer < len(values):
        opcode_and_params = str(values[pointer])
        opcode = int(opcode_and_params[-2:])
        params = opcode_and_params[:-2]

        if opcode == 1:
            # 3 params
            params = list(map(int, params.zfill(3)))
            pointer, values = add_op(pointer, values, params)

        elif opcode == 2:
            # 3 params
            params = list(map(int, params.zfill(3)))
            pointer, values = mult_op(pointer, values, params)
        elif opcode == 3:
            # 1 param
            params = list(map(int, params.zfill(1)))
            pointer, values = input_op(pointer, values, params, input_value)

        elif opcode == 4:
            # 1 param
            params = list(map(int, params.zfill(1)))
            pointer, value = output_op(pointer, values, params)
            result += str(value)

        elif opcode == 99:
            break

        pointer += 1

    return int(result)


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
