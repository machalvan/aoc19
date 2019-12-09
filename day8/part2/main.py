from utils import read_input, write_output, check_result
import re

RELATIVE_BASE = 0


def get_param_list(params, length):
    return list(map(int, params.zfill(length)))


def get_value_at_pointer(pointer, values):
    pointer += 1
    value = int(values[pointer])
    return pointer, value


def write_position_mode(pointer, values, value):
    pointer, address = get_value_at_pointer(pointer, values)

    if address < len(values):
        values[address] = value
    else:
        extend_list = [0] * ((address + 1) - len(values))
        extend_list[-1] = value
        values.extend(extend_list)

    return pointer, values


def write_relative_mode(pointer, values, value):
    pointer, address = get_value_at_pointer(pointer, values)
    address = RELATIVE_BASE + address

    if address < len(values):
        values[address] = value
    else:
        extend_list = [0] * ((address + 1) - len(values))
        extend_list[-1] = value
        values.extend(extend_list)

    return pointer, values


def write_value(pointer, values, value, param):
    if param == 0:
        pointer, values = write_position_mode(pointer, values, value)
    elif param == 2:
        pointer, values = write_relative_mode(pointer, values, value)

    return pointer, values


def read_position_mode(pointer, values):
    pointer, address = get_value_at_pointer(pointer, values)

    if address >= len(values):
        value = 0
    else:
        value = int(values[address])

    return pointer, value


def read_immediate_mode(pointer, values):
    pointer, value = get_value_at_pointer(pointer, values)
    return pointer, value


def read_relative_mode(pointer, values):
    pointer, address = get_value_at_pointer(pointer, values)
    address = RELATIVE_BASE + address

    if address >= len(values):
        value = 0
    else:
        value = int(values[address])

    return pointer, value


def read_value(param, pointer, values):
    value = 0

    if param == 0:
        pointer, value = read_position_mode(pointer, values)
    elif param == 1:
        pointer, value = read_immediate_mode(pointer, values)
    elif param == 2:
        pointer, value = read_relative_mode(pointer, values)

    return pointer, value


def add_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    sum = value1 + value2
    pointer, values = write_value(pointer, values, sum, param3)

    return pointer, values


def mult_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    product = value1 * value2
    pointer, values = write_value(pointer, values, product, param3)

    return pointer, values


def input_op(pointer, values, input_value, params):
    param = get_param_list(params, 1)[0]
    pointer, values = write_value(pointer, values, input_value, param)
    return pointer, values


def output_op(pointer, values, params):
    param = get_param_list(params, 1)[0]
    pointer, value = read_value(param, pointer, values)
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
        pointer, values = write_value(pointer, values, 1, param3)
    else:
        pointer, values = write_value(pointer, values, 0, param3)

    return pointer, values


def equals_op(pointer, values, params):
    param3, param2, param1 = get_param_list(params, 3)

    pointer, value1 = read_value(param1, pointer, values)
    pointer, value2 = read_value(param2, pointer, values)

    if value1 == value2:
        pointer, values = write_value(pointer, values, 1, param3)
    else:
        pointer, values = write_value(pointer, values, 0, param3)

    return pointer, values


def add_rel_base_op(pointer, values, params):
    global RELATIVE_BASE
    param = get_param_list(params, 1)[0]
    pointer, value = read_value(param, pointer, values)
    RELATIVE_BASE += value
    return pointer


def calc(lines):
    parser = re.compile("-?\d+")
    values = [int(x) for line in lines for x in parser.findall(line.strip())]
    result = ''
    pointer = 0
    input_value = 2

    while pointer < len(values):
        opcode_and_params = str(values[pointer])
        opcode = int(opcode_and_params[-2:])
        params = opcode_and_params[:-2]

        if opcode == 1:
            pointer, values = add_op(pointer, values, params)

        elif opcode == 2:
            pointer, values = mult_op(pointer, values, params)

        elif opcode == 3:
            pointer, values = input_op(pointer, values, input_value, params)

        elif opcode == 4:
            pointer, value = output_op(pointer, values, params)
            result += str(value)
            #break

        elif opcode == 5:
            pointer = jump_if_true(pointer, values, params)

        elif opcode == 6:
            pointer = jump_if_false_op(pointer, values, params)

        elif opcode == 7:
            pointer, value = less_than_op(pointer, values, params)

        elif opcode == 8:
            pointer, value = equals_op(pointer, values, params)

        elif opcode == 9:
            pointer = add_rel_base_op(pointer, values, params)

        elif opcode == 99:
            break

        pointer += 1

    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
