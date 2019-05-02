import numpy as np
from GameOfLifePy.src.GUI import GUI
from GameOfLifePy.src.StopWatch import StopWatch
import GameOfLifePy.src.Algorithms as Algos
import random
import time

height = 100
width = 100
iterations = 0

gui = GUI(height, width)
sw = StopWatch()

previous = []
current = np.zeros((height, width))


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


def run():
    global current, previous, iterations
    previous = current
    current = Algos.original(current)
    iterations += 1
    if np.array_equal(previous, current):
        print("ENDGAME Reached.")
        time.sleep(10)
        return
    gui.draw(current)
    gui.root.update_idletasks()
    gui.root.update()
    print("ITERATIONS: " + str(iterations) + "\n" +
          str(int(iterations / sw.get_elapsed_time_seconds() * 3600)))


current = random_fill(generate_blank(height, width))

gui.init_draw(current)

while 1 > 0:
    run()

