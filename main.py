from controller import MazeController

def main():
    print('Would you like to use following defaults:-')
    print('Window dimension 600x600')
    print('Number of rows: 10')
    print('Number of columns: 10')
    prompt = input('Answer(Y/N): ')
    if prompt.upper() == 'N':
        xDimension = int(input("Enter X Dimension of window: "))
        yDimension = int(input("Enter Y Dimension of window: "))
        rows = int(input("Enter number of rows in maze: "))
        columns = int(input("Enter number of columns in maze: "))
        
    else:
        xDimension = 600
        yDimension = 600
        rows = 20
        columns = 20

    maze_generator = MazeController(
        xDimension = xDimension, 
        yDimension = yDimension, 
        rows = rows, 
        columns = columns
        )
    maze_generator.generate_maze()

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1500)
    main()