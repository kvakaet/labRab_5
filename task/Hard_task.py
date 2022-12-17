#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

# вариант 5
if __name__ == '__main__':
    x = int(input("введите x: "))
    row = 0
    if x >= 0:
        for n in range(x + 1):
            row += (pow(-1, n) * pow(math.pi / 2, 2 * n)) / (math.factorial(2 * n) * (4 * n - 1))
        print(format(row, ".11"))
    else:
        print("ошибка")
