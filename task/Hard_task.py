#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

EPS = 1e-10

# вариант 5
if __name__ == '__main__':
    x = float(input("введите x: "))
    if x == 0:
        print("неверно введенное x", file=sys.stderr)
        exit(1)

    a = -((math.pi ** 2) / 40)
    S, n = a, 1

    while math.fabs(a) < EPS:

        a *= -((math.pi ** 2) * (4 * n - 1)) / 4 * (2 * n + 2) * (2 * n + 1) * (4 * n + 5)
        S += a
        n += 1

    print(S)
