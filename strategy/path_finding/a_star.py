from model.cell import Cell
from model.a_star_cell import AStarCell
from strategy.path_finding.path_finding_strategy import PathFindingStrategy

from queue import PriorityQueue

class AStarPathFindingStrategy(PathFindingStrategy):
    DISTANCE_BETWEEN_CELLS = 10
    def __init__(self, maze):
        self._open_set = PriorityQueue()
        self._current = None
        self._from_list = {}
        
        formatted_maze = []
        for i, row in enumerate(maze):
            formatted_maze.append([])
            for j, cell in enumerate(row):
                formatted_maze[i].append(AStarCell(cell))

        self._end = formatted_maze[5][5]
        self._end.end = True

        self._start = formatted_maze[7][2]
        self._start.cell.current = True
        start_g = 0
        start_h = self.heuristic(self._start)
        self._start.set_cost(start_g, start_h)
        self._start.start = True

        self._count = 0
        self._open_set.put((0, self._count , self._start))
        self._closed_set = [self._start]
        super().__init__(formatted_maze)

    def heuristic(self, cell):
        dx = abs(cell.column - self._end.column)
        dy = abs(cell.row - self._end.row)
        return AStarPathFindingStrategy.DISTANCE_BETWEEN_CELLS * (dx + dy)


    def get_visitable_neighbours(self):
        neighbours = []
        row = self._current.row
        column = self._current.column

        directions = {
            'up': [-1, 0],
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1]
        }

        for direction, value in directions.items():
            try:
                y = value[0]
                x = value[1]
                attempted_cell = self._maze[row+y][column +x]

                if direction == 'up':
                    if attempted_cell.cell.bottom_wall_exists():
                        continue
                elif direction == 'right':
                    if self._current.cell.right_wall_exists():
                        continue
                elif direction == 'down':
                    if self._current.cell.bottom_wall_exists():
                        continue
                elif direction == 'left':
                    if attempted_cell.cell.right_wall_exists():
                        continue

                attempted_cell.cell.computed = True
                neighbours.append(attempted_cell)
                
            except:
                continue

        return neighbours
        

    def render(self):
        neighbours = self.get_visitable_neighbours()
        print(neighbours)
        for neighbour in neighbours:
            temp_g_score = self._current.g + AStarPathFindingStrategy.DISTANCE_BETWEEN_CELLS
            if temp_g_score < neighbour.g:
                self._from_list[neighbour] = self._current

                new_g = temp_g_score
                new_h = self.heuristic(neighbour)
                neighbour.set_cost(new_g, new_h)

                if neighbour not in self._closed_set:
                    self._count += 1
                    self._open_set.put((neighbour.f, self._count, neighbour))
                    self._closed_set.append(neighbour)

    def render_completed(self):
        print(list(self._open_set.queue))
        if self._open_set.empty():
            return True
        
        if not self._current == None:
            self._current.cell.current = False

        self._current = self._open_set.get()[2]
        self._current.cell.current = True
        self._closed_set.remove(self._current)

        if self._current == self._end:
            self._current.cell.current = False
            return True
        return False

    def display_shortest_path(self):
        self._current.cell.path = True
        self._current = self._from_list[self._current]

    def display_shortest_path_completed(self):
        if self._current == self._start:
            self._current.cell.path = True
            return True
        return False

    def __str__(self):
        return 'A Star Path Finding Algorithm'