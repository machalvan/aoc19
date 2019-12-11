from utils import read_input, write_output, check_result
import re
import math
import numpy as np


class Asteroid:
    def __init__(self, x, y, frac, dxdy, gcd):
        self.x = x
        self.y = y
        self.frac = frac
        self.dxdy = dxdy
        self.gcd = gcd


def calc(lines):
    values = [[char for char in line.split()[0]] for line in lines]
    asteroids = []
    counter = 0
    x = 20
    y = 21

    for y2 in range(0, len(values)):
        for x2 in range(0, len(values[0])):
            value2 = values[y2][x2]
            south = y2 - y
            east = x2 - x

            if value2 == '.' or (south == 0 and east == 0):
                continue

            gcd = math.gcd(south, east)
            dx = int(east/gcd)
            dy = int(south/gcd)

            if dy != 0:
                frac = np.rad2deg(np.arctan(dx/dy))

                if dx < 0:
                    if dy < 0:
                        # -1, -1
                        frac = 180 - frac
                    else:
                        # -1, 1
                        frac *= -1

                else:
                    if dy < 0:
                        # 1, -1
                        frac = -180 - frac
                    else:
                        # 1, 1
                        frac *= -1

            else:
                if dx > 0:
                    frac = -90
                else:
                    frac = 90

            if dx == 0:
                if dy > 0:
                    frac = 0
                else:
                    frac = -999

            dxdy = frac
            frac += 1/10000 * gcd
            asteroid = Asteroid(x2, y2, frac, dxdy, gcd)
            asteroids.append(asteroid)

    asteroids.sort(key=lambda x: x.frac, reverse=False)

    pointer = 0
    dxdy = None
    a = None
    while counter < 200:
        asteroid = asteroids[pointer]
        a = asteroid

        if not asteroid or asteroid.dxdy == dxdy:
            pointer = (pointer + 1) % len(asteroids)
            continue

        counter += 1
        dxdy = asteroid.dxdy
        asteroids[pointer] = None
        pointer = (pointer + 1) % len(asteroids)

    return a.x * 100 + a.y


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
