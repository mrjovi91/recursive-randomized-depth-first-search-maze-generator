from tkinter import Tk
from time import sleep
from queue import LifoQueue
import random

from model import Cell
from view import MazeView


class MazeController:
    def __init__(self, xDimension, yDimension, rows, columns):
        self._root = Tk()
        self._view = MazeView()
        self._root.geometry(f"{xDimension}x{yDimension}")

        self._rows = rows
        self._columns = columns
        self._cell_x = xDimension / columns
        self._cell_y = yDimension / rows
        self._current_position = [0,0]
        self._path = LifoQueue()

        self._maze = []
        for y in range(0,rows):
            row = []
            for x in range(0,columns):
                row.append(Cell(x, y, self._cell_x, self._cell_y))
            self._maze.append(row)

        
    def make_move(self):
        directions = {
            'up': [-1, 0],
            'down': [1, 0],
            'left': [0, -1],
            'right': [0, 1]
        }
        direction = None
        while True:
            direction = random.choice(directions.keys())
            new_current_x = self._current_position[0] + directions[direction][0]
            new_current_y = self._current_position[1] + directions[direction][1]

            if (new_current_y < self._rows and
                    new_current_y >= 0 and
                    new_current_x < self._columns and 
                    new_current_x >= 0):
                continue

    def mark_current_cell(self):
        if self._maze[self._current_position[0]][self._current_position[1]].visited:
            self._maze[self._current_position[0]][self._current_position[1]].backtracked = True
        else:
            self._maze[self._current_position[0]][self._current_position[1]].visited = True




    def generate_maze(self):
        self._view.refresh(self._maze, self._current_position, self._cell_x, self._cell_y)
        self._root.update()

        self.mark_current_cell()

        
        if self.maze_is_complete:
            sleep (5)
            return True
        sleep(0.5)
        self.generate_maze()

    def maze_is_complete(self):
        for row in self._maze:
            for column in row:
                if column.visited is False or column.backtracked is False:
                    return False
        return True

