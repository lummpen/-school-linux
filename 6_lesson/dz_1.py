#!/usr/bin/python3
def b_encode(text):
    return text.encode('utf-8')

def b_decode(text):
    return text.decode('utf-8')

text_enc = b_encode(input('Введите текст: '))
text_dec = b_decode(text_enc)

print('После преобразования, получаем битовую строку:')
print(text_enc)
print('Преобразовываем в обычную строку:')
print(text_dec)