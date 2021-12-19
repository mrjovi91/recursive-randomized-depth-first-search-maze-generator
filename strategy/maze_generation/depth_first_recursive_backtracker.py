from strategy.maze_generation.maze_generation_strategy import MazeGenerationStrategy
import random
from queue import LifoQueue

class DepthFirstRecursiveBacktracker(MazeGenerationStrategy):
    def __init__(self, maze):
        self._path = LifoQueue()
        self._current_position = [0,0]
        maze[0][0].mark_as_current()
        super().__init__(maze)

    def move_to_next_cell(self):
        directions = {
            'up': [-1, 0],
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1]
        }
        current_cell = self._maze[self._current_position[0]][self._current_position[1]]
        attempted_directions = []
    
        while True:
            if all(elem in attempted_directions  for elem in directions.keys()):
                print('All nearby cells attempted')
                break
            direction = random.choice(list(directions.keys()))
            print(f'Attempting {direction}')
            if direction in attempted_directions:
                print(f'{direction} already attempted')
                continue
            attempted_directions.append(direction)

            new_current_y = self._current_position[0] + directions[direction][0]
            new_current_x = self._current_position[1] + directions[direction][1]
            attempted_cell = [new_current_y, new_current_x]
            print(f'New attempted cell: {attempted_cell}')

            if (new_current_y >= self._rows or
                    new_current_y < 0 or
                    new_current_x >= self._columns or 
                    new_current_x < 0):
                print(f'{attempted_cell} out of grid')
                continue
            
            cell = self._maze[new_current_y][new_current_x]
            if cell.visited or cell.backtracked:
                print(f'{attempted_cell} has been visited before')
                continue

            new_cell = self._maze[new_current_y][new_current_x]

            if direction == 'up':
                print(f'Destroying bottom wall of {attempted_cell}')
                new_cell.destroy_bottom_wall()
            elif direction =='right':
                print(f'Destroying right wall of {self._current_position}')
                current_cell.destroy_right_wall()
            elif direction == 'down':
                print(f'Destroying bottom wall of {self._current_position}')
                current_cell.destroy_bottom_wall()
            elif direction == 'left':
                print(f'Destroying right wall of {attempted_cell}')
                new_cell.destroy_right_wall()
            
            print(f'Adding current cell {self._current_position} to path')
            current_cell.unmark_as_current()
            self._path.put(self._current_position.copy())

            self._current_position = [new_current_y, new_current_x]
            new_cell.mark_as_current()
            print(f'Set current position to {attempted_cell}')
            return

        # If reach here, all nearby paths are visited. Time to backtrack.
        print('reached')
        self._maze[self._current_position[0]][self._current_position[1]].visited = True
        self._maze[self._current_position[0]][self._current_position[1]].backtracked = True
        current_cell.unmark_as_current()
        if not self._path.empty():
            self._current_position = self._path.get().copy()
            self._maze[self._current_position[1]][self._current_position[0]].mark_as_current()
            print(f'Backtracking to {self._current_position}')

    def mark_current_cell(self):
        if self._maze[self._current_position[0]][self._current_position[1]].visited:
            print(f'Backtracked to cell {self._current_position}')
            self._maze[self._current_position[0]][self._current_position[1]].backtracked = True
        else:
            print(f'Visited cell {self._current_position}')
            self._maze[self._current_position[0]][self._current_position[1]].visited = True

    def render(self):
        print('Marking current cell')
        self.mark_current_cell()
        print('Moving to next cell')
        self.move_to_next_cell()
        # sleep(0.125)
        print()

    def completed(self):
        start_cell = self._maze[0][0]
        print(start_cell.visited)
        print(start_cell.backtracked)
        if start_cell.visited and start_cell.backtracked:
            return True