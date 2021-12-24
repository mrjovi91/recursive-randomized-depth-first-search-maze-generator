from abc import ABC, abstractmethod

class MazeGenerationStrategy(ABC):
    def __init__(self, maze):
        self._maze = maze
        self._rows = len(maze)
        self._columns = len(maze[0])

    @abstractmethod
    def move_to_next_cell(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def completed(self):
        pass