"""
Отскакивающий от краев логотип DVD
"""
import sys, random, time

try:
    import bext
except:
    print("Программе нужен пакет bext.")
    sys.exit()

width, height = bext.size()
width = width - 1
number_of_logos = 100
pause_amount = 0.01

colors = ['red', 'green', 'blue', 'white', 'yellow', 'magenta', 'cyan']
up_right = 'ur'
up_left = 'ul'
down_right = 'dr'
down_left = 'dl'
directions = (up_left, up_right, down_left, down_right)

color = 'color'
X = 'x'
Y = 'y'
drn = 'direction'


def main():
    bext.clear()

    #Генерация логотипов
    logos = []
    for i in range(number_of_logos):
        logos.append({color: random.choice(colors),
                      X: random.randint(1, width - 4),
                      Y: random.randint(1, height - 4),
                      drn: random.choice(directions)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] = logos[-1][X] - 1
    corner_bounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')
            original_dir = logo[drn]

            if logo[X] == 0 and logo[Y] == 0:
                logo[drn] = down_right
                corner_bounces = corner_bounces + 1
            elif logo[X] == 0 and logo[Y] == height - 1:
                logo[drn] = up_right
                corner_bounces = corner_bounces + 1
            elif logo[X] == width - 3 and logo[Y] == 0:
                logo[drn] = down_left
                corner_bounces = corner_bounces + 1
            elif logo[X] == width - 3 and logo[Y] == height - 1:
                logo[drn] = up_left
                corner_bounces = corner_bounces + 1

            elif logo[X] == 0 and logo[drn] == up_left:
                logo[drn] = up_right
            elif logo[X] == 0 and logo[drn] == down_left:
                logo[drn] = down_right

            elif logo[X] == width - 3 and logo[drn] == up_right:
                logo[drn] = up_left
            elif logo[X] == width - 3 and logo[drn] == down_right:
                logo[drn] = down_left

            elif logo[Y] == 0 and logo[drn] == up_left:
                logo[drn] = down_left
            elif logo[Y] == 0 and logo[drn] == up_right:
                logo[drn] = down_right

            elif logo[Y] == height - 1 and logo[drn] == down_left:
                logo[drn] = up_left
            elif logo[Y] == height - 1 and logo[drn] == down_right:
                logo[drn] = up_right

            if logo[drn] != original_dir:
                logo[color] = random.choice(colors)

            if logo[drn] == up_right:
                logo[X] = logo[X] + 2
                logo[Y] = logo[Y] - 1
            elif logo[drn] == up_left:
                logo[X] = logo[X] - 2
                logo[Y] = logo[Y] - 1
            elif logo[drn] == down_right:
                logo[X] = logo[X] + 2
                logo[Y] = logo[Y] + 1
            if logo[drn] == down_left:
                logo[X] = logo[X] - 2
                logo[Y] = logo[Y] + 1

        bext.goto(5, 0)
        bext.fg('white')
        print('Столкновений с углами:', corner_bounces, end='')
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[color])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(pause_amount)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Отскакивающий DVD')
        sys.exit()