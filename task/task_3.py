#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Найти все трехзначные натуральные числа, сумма цифр которых равна их произведению.
if __name__ == '__main__':
    for i in range(100, 1000):
        summa = 0
        mult = 1
        num = i
        while num != 0:
            summa += num % 10
            mult *= num % 10
            num //= 10
        if summa == mult:
            print(i)
