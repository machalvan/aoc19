from utils import read_input, write_output, check_result
from itertools import permutations
import re


def get_param_list(params, length):
    return list(map(int, params.zfill(length)))


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


def read_value(param, pointer, values):
    value = 0

    if param == 0:
        pointer, value = read_position_mode(pointer, values)
    elif param == 1:
        pointer, value = read_immediate_mode(pointer, values)

    return pointer, value


def add_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    sum = value1 + value2
    pointer, values = write_position_mode(pointer, values, sum)

    return pointer, values


def mult_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    product = value1 * value2
    pointer, values = write_position_mode(pointer, values, product)

    return pointer, values


def input_op(pointer, values, input_value):
    pointer, values = write_position_mode(pointer, values, input_value)
    return pointer, values


def output_op(pointer, values, params):
    params = get_param_list(params, 1)
    pointer, value = read_value(params[0], pointer, values)
    return pointer, value


def jump_if_true(pointer, values, params):
    param2, param1 = get_param_list(params, 2)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    if value1 != 0:
        pointer = value2
        pointer -= 1

    return pointer


def jump_if_false_op(pointer, values, params):
    param2, param1 = get_param_list(params, 2)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    if value1 == 0:
        pointer = value2
        pointer -= 1

    return pointer


def less_than_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    if value1 < value2:
        pointer, values = write_position_mode(pointer, values, 1)
    else:
        pointer, values = write_position_mode(pointer, values, 0)

    return pointer, values


def equals_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    if value1 == value2:
        pointer, values = write_position_mode(pointer, values, 1)
    else:
        pointer, values = write_position_mode(pointer, values, 0)

    return pointer, values


def intcode_computer(lines, input_value1, input_value2):
    result = ''
    pointer = 0
    parser = re.compile("-?\d+")
    values = [int(x) for line in lines for x in parser.findall(line.strip())]
    input_counter = 0

    while pointer < len(values):
        opcode_and_params = str(values[pointer])
        opcode = int(opcode_and_params[-2:])
        params = opcode_and_params[:-2]

        if opcode == 1:
            pointer, values = add_op(pointer, values, params)

        elif opcode == 2:
            pointer, values = mult_op(pointer, values, params)

        elif opcode == 3:
            if input_counter == 0:
                pointer, values = input_op(pointer, values, input_value1)
            else:
                pointer, values = input_op(pointer, values, input_value2)
            input_counter += 1

        elif opcode == 4:
            pointer, value = output_op(pointer, values, params)
            result = value
            break

        elif opcode == 5:
            pointer = jump_if_true(pointer, values, params)

        elif opcode == 6:
            pointer = jump_if_false_op(pointer, values, params)

        elif opcode == 7:
            pointer, value = less_than_op(pointer, values, params)

        elif opcode == 8:
            pointer, value = equals_op(pointer, values, params)

        elif opcode == 99:
            break

        pointer += 1

    return result


def calc(lines):
    result = -1
    perm = permutations([0,1,2,3,4], 5)

    for i in list(perm):
        out = 0
        phase_settings = list(i)

        for x in range(0, 5):
            out = intcode_computer(lines, phase_settings[x], out)

        if out > result:
            result = out

    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
