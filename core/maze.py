from pprint import pprint

# Infinity used to represent a wall in the maze
INF = float("inf")

# Each cell that can be modified
class Node:
    def __init__(self):
        # Directions specifying the dege_weights
        self.neighbors = {"N": INF, "S": INF, "W": INF, "E": INF}
        return


# The maze class that we will be using to write algorithms
class Maze:
    def __init__(self, num_rows, num_columns):
        # The grid of nodes, its columns and width
        self.grid = []
        self.num_rows = num_rows
        self.num_columns = num_columns
        # Populating the grid with nodes (representing weights to adjacent nodes)
        for i in range(num_rows):
            temp = []
            for j in range(num_columns):
                temp.append(Node())
            self.grid.append(temp)
        return

    def add_path(self, start_position, direction, edge_value):
        """
        inputs:
            start_position:
                tuple of x,y position for starting node
            direction:
                N, S, E, W
            edge_value:
                the value of the edge
        """
        x, y = start_position

        # validate input coordinates
        if x not in range(0, self.num_columns) or y not in range(0, self.num_rows):
            raise Exception("Invalid coordinates.")
            return

        self.grid[y][x].neighbors[direction] = edge_value

        # validate edge addition
        if direction == "N" and 0 <= y - 1 <= self.num_rows - 1:
            self.grid[y - 1][x].neighbors["S"] = edge_value

        if direction == "S" and 0 <= y + 1 <= self.num_rows - 1:
            self.grid[y + 1][x].neighbors["N"] = edge_value

        if direction == "W" and 0 <= x - 1 <= self.num_columns - 1:
            self.grid[y][x - 1].neighbors["E"] = edge_value

        if direction == "E" and 0 <= x + 1 <= self.num_columns - 1:
            self.grid[y][x + 1].neighbors["W"] = edge_value

        return

    # display the maze as an ASCII grid
    def display(self):
        for idx, col in enumerate(self.grid[0]):
            print("+", end="")
            if col.neighbors["N"]:
                print("---", end="")
            else:
                print("   ", end="")
        print("+", end="")

        for row in self.grid:
            print()
            for idx, col in enumerate(row):
                if col.neighbors["W"]:
                    print("|", end="")
                else:
                    print(" ", end="")
                print("   ", end="")
                if idx == self.num_columns - 1 and col.neighbors["E"]:
                    print("|", end="")
            print()

            for idx, col in enumerate(row):
                print("+", end="")
                if col.neighbors["S"]:
                    print("---", end="")
                else:
                    print("   ", end="")
            print("+", end="")
        print()


# initializing a maze with 4 rows and 5 cols
maze = Maze(4, 4)

# adding test edge
maze.add_path((1, 1), "N", 0)
maze.add_path((1, 1), "W", 0)

maze.display()

