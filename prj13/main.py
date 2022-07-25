import copy
import random
import sys
import time

width = 80
height = 25

alive = '*'
dead = ' '

next_cells = {}
for x in range(width):
    for y in range(height):
        if random.randint(0, 2) == 0:
            next_cells[(x, y)] = alive
        else:
            next_cells[(x, y)] = dead

while True:
    print('\n' * 50)
    cells = copy.deepcopy(next_cells)

    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit...')

    for y in range(height):
        for x in range(width):
            left = (x - 1) % width
            right = (x + 1) % width
            above = (y - 1) % height
            below = (y + 1) % height

            num_neighbors = 0
            if cells[(left, above)] == alive:
                num_neighbors += 1
            if cells[(left, below)] == alive:
                num_neighbors += 1
            if cells[(right, above)] == alive:
                num_neighbors += 1
            if cells[(right, below)] == alive:
                num_neighbors += 1
            if cells[(x, above)] == alive:
                num_neighbors += 1
            if cells[(x, below)] == alive:
                num_neighbors += 1
            if cells[(right, y)] == alive:
                num_neighbors += 1
            if cells[(left, y)] == alive:
                num_neighbors += 1

            if cells[(x, y)] == alive and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[(x, y)] = alive
            elif cells[(x, y)] == dead and num_neighbors == 3:
                next_cells[(x, y)] = alive
            else:
                next_cells[(x, y)] = dead

    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print('Игра в жизнь Конвея')
        sys.exit()





















