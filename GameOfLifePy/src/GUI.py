from tkinter import *
from PIL import ImageTk, Image
import numpy as np


class GUI:
    #000000 - black
    #ffffff - white

    def __init__(self, height, width):
        print("GUI initialized")

        self.hex_black = "#000000"
        self.hex_white = "#FFFFFF"

        self.height = height
        self.width = width
        self.panel_array = np.zeros((self.height, self.width), dtype=object)
        self.previous = np.zeros((self.height, self.width))

        self.root = Tk()

        self.root.title("Game of Life")
        self.root.geometry(str(self.height * 7 + 10) + "x" + str(self.width * 7 + 10))
        self.board = Frame(self.root, height=self.height*7, width=self.width*7, pady=5, padx=5)
        self.canvas = Canvas(self.board, height=self.height * 7, width=self.width * 7)

        self.options = Frame(self.root, height=self.height * 7, width=340, pady=5, padx=5)

    def init_draw(self, array):
        self.previous = array
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_black)
                    self.panel_array[row][col] = panel
                else:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_white)
                    self.panel_array[row][col] = panel

        self.board.grid(column=0)
        self.options.grid(column=1)
        self.canvas.grid()

    def draw(self, array):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1 and self.previous[row][col] != 1:   # if state changed
                    self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_black)

                elif array[row][col] == 0 and self.previous[row][col] != 0:
                    self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_white)

        self.previous = array

    def update_data(self):
        self.iteration_counter #TODO ADD ITERCOUNT, START/STOP, ANOTHER ALGO
        return False
