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

    def add_edge(self, start_position, direction, edge_value):
        """
        inputs:
            start_position:
                tuple of x1,y1 position for starting node
            direction:
                N, S, E, W
            edge_value:
                the value of the edge
        """
        x1, y1 = start_position

        # checking if an edge addition
        if direction == "N" and 0 <= y1 + 1 <= self.num_rows:
            self.grid[x1][y1].neighbors[direction] = edge_value
            self.grid[x1][y1 - 1].neighbors["S"] = edge_value

        if direction == "S" and 0 <= y1 - 1 <= self.num_rows:
            self.grid[x1][y1].neighbors[direction] = edge_value
            self.grid[x1][y1 + 1].neighbors["N"] = edge_value

        if direction == "E" and 0 <= x1 + 1 <= self.num_columns:
            self.grid[x1][y1].neighbors[direction] = edge_value
            self.grid[x1 + 1][y1].neighbors["W"] = edge_value

        if direction == "W" and 0 <= x1 - 1 <= self.num_columns:
            self.grid[x1][y1].neighbors[direction] = edge_value
            self.grid[x1 - 1][y1].neighbors["E"] = edge_value

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
            print("")
            for idx, col in enumerate(row):
                if col.neighbors["W"]:
                    print("|", end="")
                print("   ", end="")
                if idx == self.num_columns - 1 and col.neighbors["E"]:
                    print("|", end="")
            print("")
            for idx, col in enumerate(row):
                print("+", end="")
                if col.neighbors["S"]:
                    print("---", end="")
                else:
                    print("   ", end="")
            print("+", end="")


# initializing a maze with 4 rows and 5 cols
maze = Maze(4, 5)

# adding test edge
maze.add_edge((0, 0), "N", 0)

maze.display()

