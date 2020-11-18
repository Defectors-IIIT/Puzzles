import sys
import random
sys.path.append("../")
from pprint import pprint
from Core.maze import Maze, INF
from queue import PriorityQueue

def Mirage(maze, p):
    """
    maze is the original maze onto which we superpose the mirage layer
    p is the probability with which we add an apparent wall
    """
    perceived_maze = Maze(maze.num_rows, maze.num_columns)
    for x in range(0, maze.num_columns):
        for y in range(0, maze.num_rows):
            # Copy the contents of the original maze
            perceived_maze.grid[x][y].neighbors = dict.copy(maze.grid[x][y].neighbors)
            
            # For each cardinal direction, check if a path exists in that direction from a particular node
            # If there is a path, then 
            if maze.grid[x][y].neighbors['W'] != INF:
                if(random.uniform(0, 1) <= p):
                    perceived_maze.add_path((x, y), 'W', INF)
                    
            if maze.grid[x][y].neighbors['E'] != INF:
                if(random.uniform(0, 1) <= p):
                    perceived_maze.add_path((x, y), 'E', INF)
            
            if maze.grid[x][y].neighbors['N'] != INF:
                if(random.uniform(0, 1) <= p):
                    perceived_maze.add_path((x, y), 'N', INF)
            
            if maze.grid[x][y].neighbors['S'] != INF:
                if(random.uniform(0, 1) <= p):
                    perceived_maze.add_path((x, y), 'S', INF)
    return perceived_maze

def check(perceived_maze, original_maze, x, y, direction):
    if perceived_maze.grid[x][y].neighbors[direction] != original_maze.grid[x][y].neighbors[direction]:
        perceived_maze.grid[x][y].neighbors[direction] = original_maze.grid[x][y].neighbors[direction]
        return True
    return False