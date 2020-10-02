from PIL import Image, ImageDraw

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
        """
        inputs:
            num_rows:
                vertical dimension of the maze grid
            num_columns:
                horizontal dimension of the maze grid
        """

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
                tuple of x, y position for starting node
            direction:
                N, S, E, W
            edge_value:
                the value of the edge
        """

        x, y = start_position

        # Validate input coordinates
        if x not in range(0, self.num_columns) or y not in range(0, self.num_rows):
            raise Exception("Invalid coordinates.")
            return

        self.grid[y][x].neighbors[direction] = edge_value

        # Validate edge addition
        if direction == "N" and 0 <= y - 1 <= self.num_rows - 1:
            self.grid[y - 1][x].neighbors["S"] = edge_value
        if direction == "S" and 0 <= y + 1 <= self.num_rows - 1:
            self.grid[y + 1][x].neighbors["N"] = edge_value
        if direction == "W" and 0 <= x - 1 <= self.num_columns - 1:
            self.grid[y][x - 1].neighbors["E"] = edge_value
        if direction == "E" and 0 <= x + 1 <= self.num_columns - 1:
            self.grid[y][x + 1].neighbors["W"] = edge_value

        return

    # to yeet
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

    def draw(self, cell_width=50, padding=10):
        """
        inputs:
            cell_width:
                dimension of each cell in the grid
            padding:
                for the outer maze edge
        """

        base_dimens = (
            padding + (self.num_columns * cell_width),
            padding + (self.num_rows * cell_width),
        )
        base = Image.new("RGB", base_dimens, (0, 0, 0))
        draw = ImageDraw.Draw(base)

        for i in range(self.num_rows):
            for j in range(self.num_columns):

                # Top left corner
                x1 = (padding / 2) + (j * cell_width)
                y1 = (padding / 2) + (i * cell_width)

                # Bottom right corner
                x2 = (padding / 2) + ((j + 1) * cell_width)
                y2 = (padding / 2) + ((i + 1) * cell_width)

                # Cell background
                draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0))

                # Cell edges
                if self.grid[i][j].neighbors["N"]:
                    draw.line((x1, y1, x2, y1), width=2)
                if self.grid[i][j].neighbors["S"]:
                    draw.line((x1, y2, x2, y2), width=2)
                if self.grid[i][j].neighbors["E"]:
                    draw.line((x2, y1, x2, y2), width=2)
                if self.grid[i][j].neighbors["W"]:
                    draw.line((x1, y1, x1, y2), width=2)

        return base
