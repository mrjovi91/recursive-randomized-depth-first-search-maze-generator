from tkinter import Tk
from time import sleep
from queue import LifoQueue
import random

from model.cell import Cell
from view.maze_view import MazeView


class MazeController:
    def __init__(self, xDimension, yDimension, rows, columns):
        self._root = Tk()
        self._view = MazeView()
        self._root.geometry(f"{xDimension}x{yDimension}")

        self._rows = rows
        self._columns = columns
        self._cell_x = xDimension / columns
        self._cell_y = yDimension / rows
        self._current_position = [0,0]
        self._path = LifoQueue()

        self._iteration = 0

        self._maze = []
        for y in range(0,rows):
            row = []
            for x in range(0,columns):
                row.append(Cell(x, y, self._cell_x, self._cell_y))
            self._maze.append(row)

    

        
    def move_to_next_cell(self):
        directions = {
            'up': [-1, 0],
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1]
        }

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

            current_cell = self._maze[self._current_position[0]][self._current_position[1]]
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
            self._path.put(self._current_position.copy())

            self._current_position[0] = new_current_y
            self._current_position[1] = new_current_x
            print(f'Set current position to {attempted_cell}')
            return

        # If reach here, all nearby paths are visited. Time to backtrack.
        self._maze[self._current_position[0]][self._current_position[1]].visited = True
        self._maze[self._current_position[0]][self._current_position[1]].backtracked = True
        if not self._path.empty():
            self._current_position = self._path.get().copy()
            print(f'Backtracking to {self._current_position}')

    def mark_current_cell(self):
        if self._maze[self._current_position[0]][self._current_position[1]].visited:
            print(f'Backtracked to cell {self._current_position}')
            self._maze[self._current_position[0]][self._current_position[1]].backtracked = True
        else:
            print(f'Visited cell {self._current_position}')
            self._maze[self._current_position[0]][self._current_position[1]].visited = True

    def generate_maze(self):
        self._iteration += 1
        print(f'Iteration: {self._iteration}')
        self._view.refresh(self._maze, self._current_position, self._cell_y, self._cell_x)
        self._root.update()
        
        if self.maze_is_complete():
            print('Maze complete!')
            self._root.mainloop()
            return

        print('Marking current cell')
        self.mark_current_cell()
        print('Moving to next cell')
        self.move_to_next_cell()
        # sleep(0.125)
        print()
        return self.generate_maze()

    def maze_is_complete(self):
        start_cell = self._maze[0][0]
        print(start_cell.visited)
        print(start_cell.backtracked)
        if start_cell.visited and start_cell.backtracked:
            return True

