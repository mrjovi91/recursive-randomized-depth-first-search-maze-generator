from tkinter import Tk
from time import sleep
from queue import LifoQueue
import random

from model.cell import Cell
from strategy.maze_generation.depth_first_recursive_backtracker import DepthFirstRecursiveBacktracker
from view.maze_view import MazeView


class MazeController:
    def __init__(self, xDimension, yDimension, rows, columns):
        self._root = Tk()
        self._view = MazeView()
        self._root.geometry(f"{xDimension}x{yDimension}")

        self._rows = rows
        self._columns = columns
        self._cell_x = xDimension / columns
        self._cell_y = yDimension / rows

        self._iteration = 0

        self._maze = []
        for y in range(0,rows):
            row = []
            for x in range(0,columns):
                row.append(Cell(x, y, self._cell_x, self._cell_y))
            self._maze.append(row)

        self._generation_strategy = DepthFirstRecursiveBacktracker(self._maze)

    def generate_maze(self):
        self._iteration += 1
        print(f'Iteration: {self._iteration}')
        self._view.refresh(self._maze, self._cell_y, self._cell_x)
        self._root.update()
        
        if self._generation_strategy.completed():
            print('Maze complete!')
            self._root.mainloop()
            return

        self._generation_strategy.render()
        return self.generate_maze()

