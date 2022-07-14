"""Дешифровщик шифра Цезаря
Перебираем все возможные ключи для подбора верного ответа"""

symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print('Введите ссобщение для дешифровки')
message = input('> ').upper()

for key in range(len(symbols)):
    translated = ''

    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)
            num -= key
            if num < 0:
                num += len(symbols)
            translated += symbols[num]
        else:
            translated += symbol

    print(f'#{key}: {translated}')
