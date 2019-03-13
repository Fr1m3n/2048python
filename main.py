from pynput import keyboard
import os
from random import choice

NEW_ELEMENTS_CHOICE = [1, 1, 2]

FIELD_WIDTH = 3
FIELD_HEIGHT = 3

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
        s = ''
        for j in i:
            el = j
            if el == 0:
                el = '.'
            s += str(el) + ' '

        print(s)


def new_game():
    pass


# render()

if __name__ == '__main__':
    spawn()
    render()
    with keyboard.Listener(
            on_press=on_press
    ) as listener:
        listener.join()
