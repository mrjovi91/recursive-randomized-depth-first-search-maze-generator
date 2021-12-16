from controller import MazeController

def main():
    maze_generator = MazeController(
        xDimension = 600, 
        yDimension = 600, 
        rows = 10, 
        columns = 10
        )
    maze_generator.generate_maze()

if __name__ == '__main__':
    main()