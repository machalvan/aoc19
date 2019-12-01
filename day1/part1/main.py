def calc(input):
    result = 0
    inputs = input.split()

    for num in inputs:
        result += int(num)

    return str(result)


def check_result(result, answer):
    if result == answer:
        print('CORRECT')
    else:
        print('EXPECTED')
        print(answer)
        print('ACTUAL')
        print(result)


def main():
    input_file = open("input.txt", "r")
    answer_file = open("answer.txt", "r")
    output_file = open("output.txt", "w")

    input = input_file.read()
    answer = answer_file.read()

    result = calc(input)
    output_file.write(result)
    check_result(result, answer)

    input_file.close()
    answer_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
