"""
Генерация календарей.
Создаёт календарь по заданному году и месяцу.
Сохраняет результат в текстовый файл, готовый для распечатки.
"""
import datetime

days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

print('Генератор календарей')

while True:
    print('Введи год для календаря')
    response = input('> ')
    year = ''

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Пожалуйста, введи год числом, например, 1234.')
    continue

while True:
    print('Введи номер месяца (от 1 до 12)')
    response = input('> ')
    if not response.isdecimal():
        print('Пожалуйста, введите число от 1 до 12, например, 4, если это Апрель')

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Пожалуйста, введите числоа от 1 до 12')


def get_calendar_for(new_year, new_month):
    cal_text = ''

    cal_text += (' ' * 49) + months[new_month - 1] + ' ' + str(new_year) + '\n'
    cal_text += '..Понедельник......Вторник.........Среда....' \
                '......Четверг........Пятница.......Суббота.......Воскресенье..\n'
    week_separator = ('+--------------' * 7) + '+\n'
    blank_row = ('|              ' * 7) + '|\n'
    current_date = datetime.date(new_year, new_month, 1)

    while current_date.weekday() != 0:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 12)
            current_date += datetime.timedelta(days=1)

        day_number_row += '|\n'
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != new_month:
            cal_text += week_separator
            return cal_text


f_cal_text = get_calendar_for(year, month)
print(f_cal_text)

calendar_filename = 'Calendar {} {}.txt'.format(month, year)
with open(calendar_filename, 'w') as f:
    f.write(f_cal_text)

print('Saved to ' + calendar_filename)
