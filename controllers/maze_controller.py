from tkinter import Tk
from time import sleep
from queue import LifoQueue
import random

from model.cell import Cell
from strategy.maze_generation.depth_first_recursive_backtracker import DepthFirstRecursiveBacktracker
from strategy.path_finding.a_star import AStarPathFindingStrategy
from strategy.path_finding.no_strategy import NoPathFindingStrategy
from view.maze_view import MazeView


class MazeController:
    def __init__(self, xDimension, yDimension, rows, columns, debug=False):
        self._debug = debug
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
        self._path_finding_strategy = AStarPathFindingStrategy(self._maze)

    def generate_maze(self):
        self._iteration += 1
        print(f'Iteration: {self._iteration}')
        self._view.refresh('maze_generation', self._maze, self._cell_y, self._cell_x)
        self._root.update()
        
        if self._generation_strategy.completed():
            print('Maze generation complete!')
            return

        self._generation_strategy.render()
        return self.generate_maze()

    def reset_iteration(self):
        self._iteration = 0

    def generate_path(self):
        self._iteration += 1
        print(f'Iteration: {self._iteration}')
        if self._path_finding_strategy.render_completed():
            self._view.refresh('path_finding', self._path_finding_strategy._maze, self._cell_y, self._cell_x)
            self._root.update()
            print('Optimal path found!')
            return
        self._path_finding_strategy.render()
        self._view.refresh('path_finding', self._path_finding_strategy._maze, self._cell_y, self._cell_x)
        self._root.update()
        return self.generate_path()

    def display_path(self):
        self._path_finding_strategy.display_shortest_path()
        self._view.refresh('path_finding', self._path_finding_strategy._maze, self._cell_y, self._cell_x)
        self._root.update()
        if self._path_finding_strategy.display_shortest_path_completed():
            self._view.refresh('path_finding', self._path_finding_strategy._maze, self._cell_y, self._cell_x)
            self._root.mainloop()
            return
        self.display_path()
        

