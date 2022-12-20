#!/usr/bin/python3
with open('./data_dz2/input.txt', 'r') as file:
    data = file.read().split()

atom_c = data[0]
atom_h = data[1]
atom_o = data[2]
dig_mol_c = int(atom_c)
dig_mol_h = int(atom_h) 
dig_mol_o = int(atom_o)

count_spirit = min(dig_mol_c, dig_mol_h, dig_mol_o)

with open('./data_dz2/output.txt', 'w') as file:
    file.write('Колличество молекул спирта = ' + str(count_spirit))

print('Формула молекулы спирта - C2H5(OH)')
print('У нас есть следующие компоненты:')
print('Атомы углерода (С) =', atom_c)
print('Атомы водорода (H) =', atom_h)
print('Атомы кислорода (O) =', atom_o)
print('Все молекулы спирта отправлены в файл, остаток компонентов:')
print('Атомы углерода (С) =', int(atom_c) - count_spirit * 2)
print('Атомы водорода (H) =', int(atom_h) - count_spirit * 6)
print('Атомы кислорода (O) =', int(atom_o) - count_spirit)