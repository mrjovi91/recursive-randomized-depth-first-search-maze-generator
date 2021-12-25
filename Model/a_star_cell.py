from model.cell import Cell

class AStarCell:
    def __init__(self, cell):
        self._cell = cell
        self._computed = False
        self._g = None # Distance from starting node
        self._h = None # Distance from end node
        self._f = None # G cost + H cost

    def set_cost(self, g, h):
        self._g = g
        self._h = h
        self._f = g + h