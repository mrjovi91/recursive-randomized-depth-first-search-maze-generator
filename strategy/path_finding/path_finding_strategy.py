from abc import ABC, abstractmethod

class PathFindingStrategy(ABC):
    def __init__(self, maze):
        self._maze = maze

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def completed(self):
        pass