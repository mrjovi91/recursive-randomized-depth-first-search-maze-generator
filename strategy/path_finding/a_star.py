from strategy.path_finding.path_finding_strategy import PathFindingStrategy

class AStarPathFindingStrategy(PathFindingStrategy):
    def __init__(self, maze):
        super().__init__(maze)

    def completed(self):
        return True