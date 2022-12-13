#!/usr/bin/python3
from random import randint
a1 = b1 = 10
a2 = b2 = 20

a = [randint(1, a2) for i in range(a1)]
b = [randint(1, b2) for i in range(b2)]
set_a = set(a)
set_b = set(b)

print('Первый отсортированный набор чисел: ', sorted(a))
print('Второй отсортированный набор чисел: ', sorted(b))
print('Выводим элементы, которые:')
print('- Входят одновременно в оба:', sorted(set_a & set_b))
print('- Входят только в первое, но не входят во второе:', sorted(set_a - set_b))
print('- Входят только во второе, но не входят в первое:', sorted(set_b - set_a))
print('- Входят в первое или во второе, но не в оба из них одновременно:', sorted(set_a ^ set_b))