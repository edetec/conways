from game import Game

import os
import time

if __name__ == '__main__':
    os.system('cls||clear')

    line = {(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)}
    glider  = {(5, 8), (4, 9), (4, 10), (5, 10), (6, 10)}
    world   = (line | glider)

    game = Game(9, 12, world)
    g_count = 1
    print('Generation: {}\n'.format(g_count))
    print(game)

    while True:
        time.sleep(0.4)
        os.system('cls||clear')

        game.next_generation()
        g_count += 1
        print('Generation: {}\n'.format(g_count))
        print(game)
