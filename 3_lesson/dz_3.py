#!/usr/bin/python3
import math
print('Квадратное уравнение имеет вид ax^2 + bx + c = 0. (где x^2 - это x в квадрате)')
a = float(input('Введите а: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

d = b ** 2 - 4 * a * c
print("Дискриминатнт D =", d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = -b / (2 * a)
    print('x =', x)
else:
    print('Корней нет')