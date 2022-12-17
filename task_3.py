#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Найти все трехзначные натуральные числа, сумма цифр которых равна их произведению.
if __name__ == '__main__':
    for i in range(100, 1000):
        _sum = 0
        _mul = 1
        num = i
        while num != 0:
            _sum += num % 10
            _mul *= num % 10
            num //= 10
        if _sum == _mul:
            print(i)
