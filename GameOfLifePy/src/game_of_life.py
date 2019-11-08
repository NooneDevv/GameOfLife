# This code is made available under the Creative Commons Zero 1.0 License (https://creativecommons.org/publicdomain/zero/1.0)
from GameOfLifePy.src.gui import GUI
import GameOfLifePy.src.algorithms as Algos
import numpy as np
import random

height = 100
width = 100

gui = GUI(height, width)


def random_fill(arr):
    """Randomly fills the initial 'board'"""
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


def run():
    current = random_fill(np.zeros((height, width)))
    gui.init_board(current)
    while True:
        gui.generation += 1
        gui.update_data()
        current = Algos.original(current)
        gui.draw(current)
        gui.root.update_idletasks()
        gui.root.update()


if __name__ == "__main__":
    run()
