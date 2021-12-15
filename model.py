class Cell:
    def __init__(self, positionX, positionY, size):
        self.visited = False
        self.backtracked = False
        self.walls = {
            'bottom': [True,  positionX*size, positionY*size + size, positionX*size + size, positionY*size + size],
            'right': [True,  positionX*size + size, positionY*size, positionX*size + size, positionY*size + size]
        }
