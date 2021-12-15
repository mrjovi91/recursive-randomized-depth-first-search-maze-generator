from tkinter import Canvas, Frame, BOTH
from model import Cell
from settings import settings

class MazeView(Frame):

    def __init__(self):
        super().__init__()
        self.master.title("Maze")
        self.pack(fill=BOTH, expand=1)
        self._canvas = Canvas(self)


    def refresh(self, maze, current_position, cell_size):
        self._canvas.delete("all")
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                color = None
                if current_position[0] == i and current_position[1] == j:
                    color = settings['current']
                elif cell.backtracked:
                    color = settings['backtracked']
                elif cell.visited:
                    color = settings['visited']

                if color is not None:
                    self._canvas.create_rectangle(
                        i*cell_size+1, 
                        j*cell_size+1, 
                        i*cell_size + cell_size, 
                        j*cell_size + cell_size, 
                        width=0,
                        fill=color
                    )

                for wall in cell.walls.values():
                    if wall[0]:
                        self._canvas.create_line(wall[1], wall[2], wall[3], wall[4])

        self._canvas.pack(fill=BOTH, expand=1)
