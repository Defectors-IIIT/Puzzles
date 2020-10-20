from os import path
from PIL import Image, ImageDraw
from json import dump as jdump, load as jload

# Directory to store generated maze dumps in
maze_store = path.dirname(path.abspath(__file__))

# Infinity used to represent a wall in the maze
INF = float("inf")

# Each cell that can be modified
class Node:
    def __init__(self, neighbors=None, color=None):
        """
        inputs:
            color:
                background color of the cell
                3-tuple of integers in the range(0, 256)
                defaults to black
        """

        # Initializing node attributes
        self.neighbors = {"N": INF, "S": INF, "W": INF, "E": INF}
        self.color = (0, 0, 0, 255)

        if neighbors:
            self.neighbors = neighbors
        if color:
            self.color = tuple(color)

        return


# The maze class that we will be using to write algorithms
class Maze:
    def __init__(self, num_rows=1, num_columns=1):
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
        for i in range(self.num_rows):
            temp = []
            for j in range(self.num_columns):
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
        base = Image.new("RGBA", base_dimens, (0, 0, 0, 255))
        draw = ImageDraw.Draw(base)

        for i in range(self.num_rows):
            for j in range(self.num_columns):

                # Top left corner coordinate
                x1 = (padding / 2) + (j * cell_width) - 1
                y1 = (padding / 2) + (i * cell_width) - 1

                # Bottom right corner coordinate
                x2 = (padding / 2) + ((j + 1) * cell_width) - 1
                y2 = (padding / 2) + ((i + 1) * cell_width) - 1

                # Cell background
                draw.rectangle((x1, y1, x2, y2), fill=self.grid[i][j].color)

                # Cell edges
                if self.grid[i][j].neighbors["N"] == INF:
                    draw.line((x1, y1, x2, y1), width=2)
                if self.grid[i][j].neighbors["S"] == INF:
                    draw.line((x1, y2, x2, y2), width=2)
                if self.grid[i][j].neighbors["W"] == INF:
                    draw.line((x1, y1, x1, y2), width=2)
                if self.grid[i][j].neighbors["E"] == INF:
                    draw.line((x2, y1, x2, y2), width=2)

        return base

    def add_colors(self, start=(0, 0), color=(255, 0, 0)):
        """
        inputs:
            start:
                specifies the starting point to color using bfs
            color:
                base color for each cell
        """

        color = (*color, 255)

        vis = []
        for i in range(0, self.num_rows):
            vis.append(list(bytearray(self.num_columns)))

        change = 1 + int(512 / (self.num_columns * self.num_rows))

        x, y = start
        self.grid[x][y].color = color
        queue = [(x, y)]

        while len(queue):
            x, y = queue[0]
            queue.pop(0)
            vis[x][y] = 1
            r, g, b, a = self.grid[x][y].color
            color = (
                r - change if r - change > 1 else 1,
                g - change if g - change > 1 else 1,
                b - change if b - change > 1 else 1,
                255,
            )

            if self.grid[x][y].neighbors["N"] != INF and vis[x - 1][y] == 0:
                queue.append((x - 1, y))
                self.grid[x - 1][y].color = color
            if self.grid[x][y].neighbors["S"] != INF and vis[x + 1][y] == 0:
                queue.append((x + 1, y))
                self.grid[x + 1][y].color = color
            if self.grid[x][y].neighbors["W"] != INF and vis[x][y - 1] == 0:
                queue.append((x, y - 1))
                self.grid[x][y - 1].color = color
            if self.grid[x][y].neighbors["E"] != INF and vis[x][y + 1] == 0:
                queue.append((x, y + 1))
                self.grid[x][y + 1].color = color

    def reset(self):
        """
        Reinitializes all the edge weights to infinity
        """

        for i in range(0, self.num_rows):
            for j in range(0, self.num_columns):
                self.grid[i][j].neighbors["N"] = INF
                self.grid[i][j].neighbors["S"] = INF
                self.grid[i][j].neighbors["E"] = INF
                self.grid[i][j].neighbors["W"] = INF

    def benchmark(self):
        """
        Deadends : only one exit/entry
        Straightways : go N-S or E-W
        Left turns : Go N-W or S-W
        Right turns : Go N-E or S-E
        Junctions : Have 3 entries/exits
        Crossroads : Have 4 entries/exits
        """

        ret = {
            "Deadends": 0,
            "Straightways": 0,
            "LeftTurns": 0,
            "RightTurns": 0,
            "Junctions": 0,
            "Crossroads": 0,
        }

        for i in range(0, self.num_rows):
            for j in range(0, self.num_columns):
                temp = self.grid[i][j].neighbors
                directions = []

                if temp["N"] != INF:
                    directions.append("N")
                if temp["S"] != INF:
                    directions.append("S")
                if temp["E"] != INF:
                    directions.append("E")
                if temp["W"] != INF:
                    directions.append("W")

                if len(directions) == 1:
                    ret["Deadends"] += 1
                elif len(directions) == 4:
                    ret["Crossroads"] += 1
                elif len(directions) == 3:
                    ret["Junctions"] += 1
                elif "N" in directions and "S" in directions:
                    ret["Straightways"] += 1
                elif "E" in directions and "W" in directions:
                    ret["Straightways"] += 1
                elif "W" in directions:
                    ret["LeftTurns"] += 1
                elif "E" in directions:
                    ret["RightTurns"] += 1
        return ret

    def dump(self, filename):
        """
        inputs:
            filename:
                to dump the maze into
        """

        # Serialize maze into a json object
        serialized = list(
            map(
                lambda row: [{"neighbors": col.neighbors} for col in row],
                self.grid,
            )
        )

        with open(path.join(maze_store, "Generated", filename), "w") as maze_dump:
            jdump(serialized, maze_dump)

    def load(self, filename):
        """
        inputs:
            filename:
                to load maze from
        """

        with open(path.join(maze_store, "Generated", filename), "r") as maze_load:
            maze = jload(maze_load)

        # Set maze dimensions from file
        self.grid = []
        self.num_columns = len(maze[0])
        self.num_rows = len(maze)

        # Populating the grid with loaded nodes
        for i in range(self.num_rows):
            temp = []
            for j in range(self.num_columns):
                temp.append(Node(neighbors=maze[i][j]["neighbors"], color=[0, 0, 0]))
            self.grid.append(temp)

        return
