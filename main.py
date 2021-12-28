from controllers.maze_controller import MazeController

def main():
    print('Would you like to use following defaults:-')
    print('Window dimension 600x600')
    print('Number of rows: 20')
    print('Number of columns: 20')
    prompt = input('Answer(Y/N): ')
    if prompt.upper() == 'N':
        xDimension = int(input("Enter X Dimension of window: "))
        yDimension = int(input("Enter Y Dimension of window: "))
        rows = int(input("Enter number of rows in maze: "))
        columns = int(input("Enter number of columns in maze: "))
        
    else:
        xDimension = 600
        yDimension = 600
        rows = 10
        columns = 10

    maze_generator = MazeController(
        xDimension = xDimension, 
        yDimension = yDimension, 
        rows = rows, 
        columns = columns
        )
    maze_generator.generate_maze()
    maze_generator.reset_iteration()
    print()
    print('Solving maze...')
    maze_generator.generate_path()
    maze_generator.display_path()

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)
    main()