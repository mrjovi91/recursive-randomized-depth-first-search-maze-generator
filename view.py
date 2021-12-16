from tkinter import Canvas, Frame, BOTH
from model import Cell
from settings import settings

class MazeView(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Maze")
        self.pack(fill=BOTH, expand=1)
        self._canvas = Canvas(self)


    def refresh(self, maze, current_position, cell_y, cell_x):
        self._canvas.delete("all")
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                color = None
                if current_position[1] == x and current_position[0] == y:
                    color = settings['current']
                elif cell.backtracked:
                    color = settings['backtracked']
                elif cell.visited:
                    color = settings['visited']

                if color is not None:
                    self._canvas.create_rectangle(
                        x*cell_x + 1, 
                        y*cell_y + 1, 
                        x*cell_x + cell_x, 
                        y*cell_y + cell_y, 
                        width=0,
                        fill=color
                    )

                for wall in cell.walls.values():
                    if wall[0]:
                        self._canvas.create_line(wall[1], wall[2], wall[3], wall[4])

        self._canvas.pack(fill=BOTH, expand=1)
