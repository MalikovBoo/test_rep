import random
import time


guess_count = 10


def rules():
    s = "Добро пожаловать в игру Bagles \n" \
        "Это дедуктивная логическая игра. \n" \
        "Вам будет загадано 3-значное число. Попробуйте его угадать. \n \n" \
        "Вот некоторые подсказки: \n" \
        "Когда я скажу:       Это значит: \n" \
        "Pico                 Одна из цифр верно угадана, но не на своем месте. \n" \
        "Fermi                Одна из цифр верно угадана и она на своем месте. \n" \
        "Bagels               Нет верно угаданных цифр. \n \n" \
        "Число загадано. \n" \
        "У вас есть " + str(guess_count) + " попыток, чтобы его угадать."
    for i in s.split("\n"):
        print(i)
        time.sleep(1)


def guess_try(correct, new_answ):
    answ_list = []
    if correct == new_answ:
        return "Всё верно!"
    else:
        for i in range(3):
            if correct[i] == new_answ[i]:
                answ_list.append("Fermi")
            elif correct[i] in new_answ:
                answ_list.append("Pico")
        if not answ_list:
            answ_list.append("Bagels")
        answ_list.sort()
        answ_list = " ".join(answ_list)
        return answ_list


def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers)
    secret_num = ""
    for i in range(3):
        secret_num = secret_num + str(numbers[i])
    return secret_num


def game(count):
    while True:
        i = 1
        correct_answ = get_secret_num()
        while i < count:
            print("Попытка №" + str(i))
            answ = input("> ")
            if len(answ) == 3:
                str_result = guess_try(correct_answ, answ)
            else:
                str_result = "Введено некорректное число"
            print(str_result)
            if str_result == "Всё верно!":
                break
            else:
                i = i + 1
        if i == count:
            print("Увы, но не получилось. \nВерный ответ: {}".format(correct_answ))
        print("Хочешь сыграть ещё раз? (да или нет)")
        if input("> ").lower() != "да":
            print("Спасибо за игру!")
            break
        else:
            print("Поехали ещё разок! \n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rules()
    game(guess_count)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
