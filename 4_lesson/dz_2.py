#!/usr/bin/python3
colors = { 'Red' : (255, 0, 0), '#FF0000' : (255, 0, 0), 'Pink' : (255, 192, 203), '#FFC0CB' : (255, 192, 203), 'Blue' : (0, 0, 255), '#0000FF' : (0, 0, 255), 'Yellow' : (255, 255, 0), '#FFFF00' : (255, 255, 0), 'Purple' : (128, 0, 128), '#800080' : (128, 0, 128), }
print('Введите наименование цвета. (Red, Pink, Blue, Yellow, Purple)')
d = input('Наименовние цвета: ')
f = colors.get(d, 'данного цвета нет в базе')
print(d, '-', f)