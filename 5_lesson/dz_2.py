#!/usr/bin/python3
from decimal import Decimal


def sum_numbers(num):
    sum = 0
    for i in num:
        try:
            sum += Decimal(i)
        except:
            error.append(i)

    print('Данные параметры с числами не удалось суммировать:', error, sep='\n')

    return print('Сумма всех чисел =', sum)


value = []
error = []

print('Найдем сумму всех вводимых параметров. Как только ввод будет завершен, напишите: стоп')

while True:
    x = input('Вводим параметр:')
    if x == 'стоп':
        break
    else:
        value.append(x)

sum_numbers(value)