from pynput import keyboard
import os
from random import choice
from colorama import init, Fore, Back, Style


# colorama init
init(autoreset=True)

NEW_ELEMENTS_CHOICE = [1, 1, 2]

COLORS = {
    '.': Fore.WHITE,
    0: Fore.WHITE,
    1: Fore.WHITE,
    2: Fore.BLUE,
    4: Fore.CYAN,
    8: Fore.GREEN,
    16: Fore.RED,
    32: Fore.YELLOW,
    64: Fore.MAGENTA,
    128: Fore.LIGHTGREEN_EX,
    256: Fore.LIGHTBLUE_EX,
    512: Fore.LIGHTRED_EX,
    1024: Fore.LIGHTYELLOW_EX,
    2048: Fore.LIGHTCYAN_EX
}

FIELD_WIDTH = 3
FIELD_HEIGHT = 3


# generating field
field = [[0 for j in range(FIELD_WIDTH)] for i in range(FIELD_HEIGHT)]


def on_press(key):
    # print(key)
    if key == keyboard.Key.esc:
        exit(0)
    do_turn(key)


def do_turn(key):
    if key == keyboard.Key.up:
        for i in range(FIELD_HEIGHT):
            for j in range(FIELD_WIDTH):
                el = field[i][j]
                delta = 0
                while True:
                    new_delta = delta + 1
                    if i - new_delta < 0:
                        break
                    if field[i - new_delta][j] != 0 and field[i - new_delta][j] != el:
                        break
                    delta = new_delta
                if delta != 0:
                    field[i - delta][j] += el
                    field[i][j] = 0

    elif key == keyboard.Key.down:
        for i in reversed(range(FIELD_HEIGHT)):
            for j in range(FIELD_WIDTH):
                el = field[i][j]
                delta = 0
                while True:
                    new_delta = delta - 1
                    if i - new_delta > FIELD_HEIGHT - 1:
                        break
                    if field[i - new_delta][j] != 0 and field[i - new_delta][j] != el:
                        break
                    delta = new_delta
                if delta != 0:
                    field[i - delta][j] += el
                    field[i][j] = 0

    elif key == keyboard.Key.left:
        for i in range(FIELD_WIDTH):
            for j in range(FIELD_HEIGHT):
                el = field[i][j]
                if el == 0:
                    continue
                delta = 0
                while True:
                    new_delta = delta + 1
                    if j - new_delta < 0:
                        break
                    if field[i][j - new_delta] != 0 and field[i][j - new_delta] != el:
                        break
                    delta = new_delta
                # print(delta)
                if delta != 0:
                    field[i][j - delta] += el
                    field[i][j] = 0

    elif key == keyboard.Key.right:
        for i in reversed(range(FIELD_WIDTH)):
            for j in range(FIELD_HEIGHT):
                el = field[i][j]
                if el == 0:
                    continue
                delta = 0
                while True:
                    new_delta = delta - 1
                    if j - new_delta > FIELD_WIDTH - 1:
                        break
                    if field[i][j - new_delta] != 0 and field[i][j - new_delta] != el:
                        break
                    delta = new_delta
                # print(delta)
                if delta != 0:
                    field[i][j - delta] += el
                    field[i][j] = 0

    spawn()
    render()


def spawn():
    free_space = []
    for ind, i in enumerate(field):
        for qeq, j in enumerate(i):
            if j == 0:
                free_space.append((ind, qeq))
    if len(free_space) == 0:
        return False
    index = choice(free_space)
    value = choice(NEW_ELEMENTS_CHOICE)
    field[index[0]][index[1]] = value

    return True


def render():
    os.system('cls')
    for i in field:
        els = []
        for j in i:
            el = j
            if el == 0:
                el = '.'
            el = COLORS[j] + str(el)

            els.append(str(el))
        print('')
        s = ' '.join(['{:^15}' for i in els])
        # print(s)
        # print(els)
        print(s.format(*els))


def new_game():
    pass


if __name__ == '__main__':
    spawn()
    render()
    with keyboard.Listener(
            on_press=on_press
    ) as listener:
        listener.join()
