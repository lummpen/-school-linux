#!/usr/bin/python3
import os

print(f'Наименование операционной системы: {os.name}')
print(f'Имя пользователя: {os.getlogin()}')
print(f'Cписок файлов и директорий в папке: {os.listdir(os.getcwd())}')