"""A collection of algorithms used for Game Of Life"""

from contextlib import suppress
import numpy as np


def original(arr):
    """Calculates the next state of a given 'board' following the classic rules of Conway's Game Of Life"""
    height = np.shape(arr)[0]
    width = np.shape(arr)[1]
    result = np.array(arr)

    for row in range(height):
        for col in range(width):
            neighbors = 0
            val = result[row][col]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if row + i < 0 or col + j < 0 or row + i > height or col + j > width:
                        continue
                    with suppress(IndexError):
                        if arr[row + i][col + j] == 1:
                            neighbors += 1

            if neighbors == 3 and val == 0:
                result[row][col] = 1

            elif neighbors > 3 and val == 1 or neighbors < 2 and val == 1:
                result[row][col] = 0

    return result
