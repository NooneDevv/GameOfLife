from GameOfLifePy.src.GUI import GUI
import GameOfLifePy.src.algorithms as Algos
import numpy as np
import random

CLIENT_ID = "60306b2232b458d"
CLIENT_SECRET = "af83504989ead81d07e49ea89f27f541f032411d"
height = 100
width = 100

gui = GUI(height, width)


def generate_blank(h, w):
    return np.zeros((h, w))


def random_fill(arr):
    h = np.shape(arr)[0]  # NUMBER OF ROWS
    w = np.shape(arr)[1]
    result = np.zeros((h, w))

    for row in range(0, h):
        for col in range(0, w):
            if random.choice([0, 1]) == 1:
                result[row][col] = 1
            else:
                result[row][col] = 0
    return result


current = random_fill(generate_blank(height, width))
gui.init_board(current)


def run():
    global current
    while True:
        gui.generation += 1
        gui.update_data()
        current = Algos.original(current)
        gui.draw(current)
        gui.root.update_idletasks()
        gui.root.update()


if __name__ == "__main__":
    run()
