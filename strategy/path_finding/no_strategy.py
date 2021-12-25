from strategy.path_finding.path_finding_strategy import PathFindingStrategy

class NoPathFindingStrategy(PathFindingStrategy):
    def __init__(self, maze):
        super().__init__(maze)

    def render(self):
        pass

    def completed(self):
        return True