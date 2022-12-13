#!/usr/bin/python3 
n = 7
a = [3, 5, 1, 2, 4, 7, 8, 9]
print('Изначально список такого вида:', a)
for start in range(n - 1):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)
