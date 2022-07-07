"""Шифр Цезаря
Шифр Цезаря — шифр сдвига, в котором шифрование и дешифровка букв
производятся путем сложения и вычитания соответствующих чисел.
Дополнительная информация: https://ru.wikipedia.org/wiki/Шифр_Цезаря"""


symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


print('Работа с шифром Цезаря \n'
      'шифр Цезаря работает за счет сдвига символов в слове на определенное заданное колчиество символов \n'
      'Например, для заданного ключа 3 буква А станет буквой Г, Б превратиться в Е и т.д. ')
print()

while True:
    print('(E)Шифруем или (D)дешифруем?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Пожалуйста, введи букву D или E')

print('Ключ для сдвига при шифровке или дешифровке:')
while True:
    max_key = len(symbols) - 1
    print('Пожалуйста, введи число-ключ от (0 до {}).'.format(max_key))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) <= max_key:
        key = int(response)
        break

print('Введи сообщение для обработки (шифровки/расшифровки):')
message = input('> ').upper()

translated = ''

for symbol in message:
    if symbol in symbols:
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        if num >= max_key:
            num -= max_key
        elif num < 0:
            num += max_key
        translated += symbols[num]
    else:
        translated += symbol
print(translated)
