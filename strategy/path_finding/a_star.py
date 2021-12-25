from model.cell import Cell
from model.a_star_cell import AStarCell
from strategy.path_finding.path_finding_strategy import PathFindingStrategy

class AStarPathFindingStrategy(PathFindingStrategy):
    def __init__(self, maze):
        formatted_maze = []
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                formatted_maze[i][j] = AStarCell(cell)

        super().__init__(formatted_maze)

    def render(self):
        pass

    def completed(self):
        return True