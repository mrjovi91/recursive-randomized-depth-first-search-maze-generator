class Cell:
    def __init__(self, positionX, positionY, cell_x, cell_y):
        self.visited = False
        self.backtracked = False
        self.walls = {
            'bottom': [True,  positionX*cell_x, positionY*cell_y + cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y],
            'right': [True,  positionX*cell_x + cell_x, positionY*cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y]
        }
