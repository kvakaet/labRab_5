#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Симметричны ли точки M1(x1, y1) и M2(x2, y2) относительно оси Оx или относительно оси Оy?
if __name__ == '__main__':
    x1 = int(input("введите координаты точки M1 \n"))
    y1 = int(input())
    x2 = int(input("введите координаты точки M2 \n"))
    y2 = int(input())

    if x1 == x2 and y1 == -y2:
        print("точки симметричны оси Оx")
    else:
        print("точки не симметричны оси Оx")
    if x1 == -x2 and y1 == y2:
        print("точки симметричны оси Оy")
    else:
        print("точки не симметричны оси Оy")
