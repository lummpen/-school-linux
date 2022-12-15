#!/usr/bin/python3
def password(pas):
    f1 = f2 = f3 = False
    for i in list(pas):
        if i.isdigit():
            f1 = True
        elif not i.isdigit():
            f2 = True
    if 'password' not in pas.lower():
        f3 = True
    if len(pas) >= 6 and f1 and f2 and f3:
        return True
    else:
        return False


print('Условия пароля:')
print('- не менее 6 символов;')
print('- содержит хотя бы одну цифру')
print('- не должен состоять только из цифр;')
print('- не должен содержать слово “password” в любом регистре.')
x = password(input('Введите пароль: '))

if x:
    print('пароль надежный')
else:
    print('пароль не надежный')