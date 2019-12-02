from utils import read_input, write_output, check_result


def calc(lines):
    result = ''
    for word in lines.split():
        print(word)  # Code here
    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
