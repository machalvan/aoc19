from utils import read_input, write_output, check_result
import re
import math


def calc(lines):
    values = [[char for char in line.split()[0]] for line in lines]
    most_asteroids = []
    loc = ()

    for y in range(0, len(values)):
        for x in range(0, len(values[0])):
            asteroids = []
            value = values[y][x]

            if value == '.':
                continue

            for y2 in range(0, len(values)):
                for x2 in range(0, len(values[0])):
                    value2 = values[y2][x2]
                    south = y2 - y
                    east = x2 - x

                    if value2 == '.' or (south == 0 and east == 0):
                        continue

                    gcd = math.gcd(south, east)
                    asteroid = (int(south/gcd), int(east/gcd))

                    if asteroid not in asteroids:
                        asteroids.append(asteroid)

            if len(asteroids) > len(most_asteroids):
                most_asteroids = asteroids
                loc = (x, y)

    print(loc)
    result = len(most_asteroids)
    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
