from tkinter.constants import X


class Cell:
    def __init__(self, positionX, positionY, cell_x, cell_y):
        self.positionX = positionX
        self.positionY = positionY
        self.current = False
        self.visited = False
        self.backtracked = False
        self.walls = {
            'bottom': [True,  positionX*cell_x, positionY*cell_y + cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y],
            'right': [True,  positionX*cell_x + cell_x, positionY*cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y]
        }

    def bottom_wall_exists(self):
        return self.walls['bottom'][0]

    def right_wall_exists(self):
        return self.walls['right'][0] 

    def destroy_bottom_wall(self):
        self.walls['bottom'][0] = False

    def destroy_right_wall(self):
        self.walls['right'][0] = False

    def mark_as_current(self):
        self.current = True

    def unmark_as_current(self):
        self.current = False

