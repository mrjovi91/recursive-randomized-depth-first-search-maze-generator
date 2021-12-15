from tkinter import Tk
from time import sleep

from model import Cell
from view import MazeView
from queue import LifoQueue

class MazeController:
    def __init__(self):
        self._root = Tk()
        self._view = MazeView()
        self._root.geometry("600x600")
        self._cell_size = 60
        self._current_position = [0,0]
        self._path = LifoQueue()

        self._maze = []
        for i in range(0,10):
            row = []
            for j in range(0,10):
                row.append(Cell(i, j, self._cell_size))
            self._maze.append(row)

        

    def generate_maze(self):
        # Incomplete code block for recursive maze generation
        while True:
            try:
                break
            except:
                continue

        self._view.refresh(self._maze, self._current_position, self._cell_size)
        self._root.update()
        
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

