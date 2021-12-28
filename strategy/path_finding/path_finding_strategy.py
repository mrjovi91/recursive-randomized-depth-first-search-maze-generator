from abc import ABC, abstractmethod

class PathFindingStrategy(ABC):
    def __init__(self, maze):
        self._maze = maze

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def render_completed(self):
        pass

    @abstractmethod
    def display_shortest_path(self):
        pass

    @abstractmethod
    def display_shortest_path_completed(self):
        pass