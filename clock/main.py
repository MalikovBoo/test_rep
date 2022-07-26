import time
import datetime
import sevseg


def time_draw(hour, minute, second):
    h_digits = sevseg.getSevSegStr(hour, 2)
    h_high_str, h_mid_str, h_low_str = h_digits.splitlines()

    m_digits = sevseg.getSevSegStr(minute, 2)
    m_high_str, m_mid_str, m_low_str = m_digits.splitlines()

    s_digits = sevseg.getSevSegStr(second, 2)
    s_high_str, s_mid_str, s_low_str = s_digits.splitlines()

    print(h_high_str + '   ' + m_high_str + '   ' + s_high_str)
    print(h_mid_str + ' * ' + m_mid_str + ' * ' + s_mid_str)
    print(h_low_str + ' * ' + m_low_str + ' * ' + s_low_str)


def start_clock():
    while True:
        now = datetime.datetime.now()
        h = '{:02}'.format(now.hour)
        m = '{:02}'.format(now.minute)
        s = '{:02}'.format(now.second)
        time_draw(h, m, s)
        time.sleep(1)
        print('\n' * 60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_clock()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
