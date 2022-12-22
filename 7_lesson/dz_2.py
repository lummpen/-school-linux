#!/usr/bin/python3
import random
import numpy

matrix = numpy.random.randint(0, 50, (3, 3))
print(matrix)

print('Матрицы:' + '\n' + str(matrix.transpose()))