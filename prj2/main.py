import datetime, random


def description():
    s = ("Парадокс дней рождения! \n"
         "Парадоск показывает, что даже в небольшой группе есть люди, чьи дни рождения совпадают.\n"
         "Эта программе симулирует эксперименты Монте-Карло. \n"
         "Но на самом деле это не парадокс, а просто неожиданный результат.")


def get_birthdays(count):
    bd_list = []
    for i in range(count):
        start_of_year = datetime.date(2001, 1, 1)
        rand_day = datetime.timedelta(random.randint(0, 364))
        bd = start_of_year + rand_day
        bd_list.append(bd)
    return bd_list


def get_match(bd_list):
    if len(bd_list) == len(set(bd_list)):
        return None

    while len(bd_list)>0:
        if bd_list.pop(0) in bd_list:
            return "Yes"



print(description())

month = ("январь", "февраль",
         "март", "апрель", "май",
         "июнь", "июль", "август",
         "сентябрь", "октябрь", "ноябрь",
         "декабрь")

numBDays = 100
while True:
    print("Сколько людей будет в группе? (Не более 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print("Вот получившиеся {} дней рождения:".format(numBDays))
birthdays = get_birthdays(numBDays)
for i, bd in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    month_name = month[bd.month - 1]
    date_text = "{} {}".format(month_name, bd.day)
    print(date_text, end="")
print()
print()

match = get_match(birthdays)

if match is not None:
    print("В этой группе есть люди с одинаковыми днями рождения.")
else:
    print("В этой группе совпадений нет.")
print()

print("Смоделируем ситуацию 100_000 раз...")
input("Нажмите Enter, чтобы начать")

print("Поехали! 100_000 симуляций ждут нас...")
print()

sim_match = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "симуляций уже прошло...")
    birthdays = get_birthdays(numBDays)
    if get_match(birthdays):
        sim_match = sim_match + 1
print("100_000 симуляций проведено.")
print()
print()

probability = round(sim_match/100_000 * 100,2)
print("На 100_000 симуляций с группами по {} людей".format(numBDays))
print("Совпадений было {}. Это значит, что...".format(sim_match))
print("в группе из {} человек с вероятностью в {}%".format(numBDays, probability))
print("есть люди с одинаковыми днями рождения.")
print()
print("Эти результаты могут удивить!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
