from tkinter import *
from GameOfLifePy.src.StopWatch import StopWatch
import numpy as np


class GUI:
    #000000 - black
    #ffffff - white

    def __init__(self, height, width):
        print("GUI initialized")

        self.sw = StopWatch()

        self.hex_black = "#000000"
        self.hex_white = "#FFFFFF"
        self.generation = 0

        self.height = height
        self.width = width
        self.panel_array = np.zeros((self.height, self.width), dtype=object)
        self.previous = np.zeros((self.height, self.width))

        self.root = Tk()
        self.iterations_count = StringVar()

        self.root.title("Game of Life")
        self.root.geometry(str(self.height * 7 + 100) + "x" + str(self.width * 7 + 30))

        self.board = Frame(self.root, height=self.height*7, width=self.width*7, pady=5, padx=5)
        self.canvas = Canvas(self.board, height=self.height * 7, width=self.width * 7)

        self.options = Frame(self.root, height=self.height * 7, width=340, pady=5, padx=5)
        self.start_stop_button = Button(self.options, width=20, height=5, text="Start", bg="grey")
        self.iter_count = Label(self.options, textvariable=self.iterations_count, width=25)

    def print_data(self):
        print("ITERATIONS: " + str(self.iterations) + "\n" +
              str(int(self.iterations / self.sw.get_elapsed_time_seconds() * 3600)))

    def init_gui(self, array):
        self.previous = array
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_black)
                    self.panel_array[row][col] = panel
                else:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_white)
                    self.panel_array[row][col] = panel

        self.board.grid(column=0, row=0)
        self.options.grid(column=1, row=0)
        self.canvas.grid()
        self.start_stop_button.grid(row=0)
        self.iter_count.grid(row=1)

    def draw(self, array):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if array[row][col] == 1 and self.previous[row][col] != 1:   # if state changed
                    self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_black)

                elif array[row][col] == 0 and self.previous[row][col] != 0:
                    self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_white)

        self.previous = array

    def update_data(self):
        self.iterations_count.set("Generation: " + str(self.generation))
