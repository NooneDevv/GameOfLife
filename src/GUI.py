from tkinter import *
from PIL import ImageTk, Image
import numpy as np


class GUI:

    def __init__(self, height, width):
        print("GUI initialized")

        self.height = height
        self.width = width
        self.panel_array = np.zeros((self.height, self.width), dtype=object)
        self.previous = np.zeros((self.height, self.width))

        self.root = Tk()

        self.bl = Image.open("/home/n/Pictures/black.png")
        self.wh = Image.open("/home/n/Pictures/white.png")
        self.black = ImageTk.PhotoImage(self.bl)
        self.white = ImageTk.PhotoImage(self.wh)

        self.root.title("Game of Life")
        self.root.geometry(str(height * 7 + 10) + "x" + str(width * 7 + 10))
        self.board = Frame(self.root, height=height*7, width=width*7, pady=5, padx=5)
        self.options = Frame(self.root, height=height * 7, width=width * 7, pady=5, padx=5)

    def init_draw(self, array):
        self.previous = array
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1:
                    panel = Label(self.board, image=self.black)
                    panel.image = self.black
                    self.panel_array[row][col] = panel
                    panel.grid(row=row, column=col)
                else:
                    panel = Label(self.board, image=self.white)
                    panel.image = self.white
                    self.panel_array[row][col] = panel
                    panel.grid(row=row, column=col)
        self.board.grid(row=0)
        self.options.grid(row=1)

    def draw(self, array):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1 and self.previous[row][col] != 1:   # if state changed
                    self.panel_array[row][col].configure(image=self.black)
                elif array[row][col] == 0 and self.previous[row][col] != 0:
                    self.panel_array[row][col].configure(image=self.white)

        self.previous = array

    def update_data(self):
        self.iteration_counter #TODO ADD ITERCOUNT, START/STOP, ANOTHER ALGO
        return False
