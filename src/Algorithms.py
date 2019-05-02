import numpy as np


def original(arr):
    size = np.array(arr)
    height = np.shape(size)[0]  # NUMBER OF ROWS
    width = np.shape(size)[1]  # NUMBER OF COLS

    result = np.zeros((height, width))

    for row in range(0, height):
        for col in range(0, width):
            neighbors = 0
            val = arr[row][col]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if i == 0 and j == 0:
                            continue
                        if row + i < 0 or col + j < 0 or row + i > height or col + j > width:
                            continue
                        if arr[row + i][col + j] == 1:
                            neighbors += 1
                    except IndexError:
                        pass

            if neighbors == 3 and val == 0: #4 COMES ALIVE
                result[row][col] = 1

            elif neighbors > 3 and val == 1: # 2 OVERCROWDING
                result[row][col] = 0

            elif 2 <= neighbors <= 3 and val == 1: #3 LIVES ON
                result[row][col] = 1

            elif neighbors < 2: #DIES #1
                result[row][col] = 0

    return result
