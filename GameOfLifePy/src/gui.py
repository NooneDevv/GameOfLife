from tkinter import *
from GameOfLifePy.src.stopwatch import StopWatch
import numpy as np
import random


class GUI:

    def __init__(self, height, width):
        print("GUI initialized")

        self.sw = StopWatch()

        self.hex_black = "#000000"
        self.hex_white = "#FFFFFF"
        self.height = height
        self.width = width
        self.generation = 0
        self.cell_count = 0
        self.running = True

        self.panel_array = np.zeros((self.height, self.width), dtype=object)
        self.previous = np.zeros((self.height, self.width))

        self.root = Tk()

        self.iterations_count = StringVar()
        self.iterations_per_hour = StringVar()
        self.time_elapsed = StringVar()
        self.cells_alive = StringVar()
        self.cells_dead = StringVar()

        self.root.title("Game of Life")
        self.root.geometry(str(self.height * 7 + 240) + "x" + str(self.width * 7 + 10))
        # FRAMES
        self.board = Frame(self.root, height=self.height*7, width=self.width*7, pady=5, padx=5)
        self.options = Frame(self.root, height=self.height * 7, width=340, pady=5, padx=5)
        self.canvas = Canvas(self.board, height=self.height * 7, width=self.width * 7)
        # "STATIC" ELEMENTS
        self.start_stop_button = Button(self.options, width=10, height=2, text="Start", bg="grey", fg="black")
        self.reset_button = Button(self.options, width=10, height=2, text="Reset", bg="grey", fg="black",
                                   command=self.reset)
        self.iter_label = Label(self.options, textvariable=self.iterations_count, width=25, relief="sunken")
        self.iter_ph_label = Label(self.options, textvariable=self.iterations_per_hour, width=25, relief="sunken")
        self.time_label = Label(self.options, textvariable=self.time_elapsed, width=25, relief="sunken")
        self.cells_alive_label = Label(self.options, textvariable=self.cells_alive, width=25, relief="sunken")
        self.cells_dead_label = Label(self.options, textvariable=self.cells_dead, width=25, relief="sunken")

        self.init_gui()

    def init_board(self, arr):
        self.previous = arr
        for row in range(self.height):
            for col in range(self.width):
                if arr[row][col] == 1:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_black)
                    self.panel_array[row][col] = panel
                else:
                    panel = self.canvas.create_rectangle(row*7, col*7, row*7+7, col*7+7, fill=self.hex_white)
                    self.panel_array[row][col] = panel

        self.board.grid(column=0, row=0)
        self.options.grid(column=1, row=0)
        self.canvas.grid()

    def init_gui(self):
        self.start_stop_button.grid(row=0, pady=10, sticky="N")
        self.reset_button.grid(row=0, column=1, pady=10, sticky="N")
        self.iter_label.grid(row=1, columnspan=2, pady=5)
        self.cells_alive_label.grid(row=2, columnspan=2, pady=5)
        self.cells_dead_label.grid(row=3, columnspan=2, pady=5)
        self.iter_ph_label.grid(row=4, columnspan=2, pady=5)
        self.time_label.grid(row=5, columnspan=2, pady=5)

    def draw(self, array):
        self.cell_count = np.count_nonzero(array == 1)
        if self.running:
            for row in range(self.height):
                for col in range(self.width):
                    if array[row][col] == 1 and self.previous[row][col] != 1:   # if state changed
                        self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_black)

                    elif array[row][col] == 0 and self.previous[row][col] != 0:
                        self.canvas.itemconfig(self.panel_array[row][col], fill=self.hex_white)

            self.previous = array

    def update_data(self):
        self.iterations_count.set(f"Generation: {self.generation}")
        self.iterations_per_hour.set(f"Ticks per hour: {int(self.generation / self.sw.get_elapsed_time_seconds() * 3600)}")
        self.time_elapsed.set(f"Time elapsed: {self.sw.get_elapsed_time()}")
        self.cells_alive.set(f"Cells alive: {self.cell_count}")
        self.cells_dead.set(f"Cells dead: {str(self.height*self.width-self.cell_count)}")

    def reset(self):
        self.generation = 0
        self.sw.reset()

