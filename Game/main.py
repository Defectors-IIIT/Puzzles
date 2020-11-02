# imports {{{
import sys
import pygame
from Wall import Wall

sys.path.append("../")
from Core.maze import Maze, INF

# }}}

# color codes {{{
colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    "VIOLET": (255, 0, 255),
    "YELLOW": (255, 255, 0),
}
# }}}

# pygame setup {{{
pygame.init()

screen_dimens = (500, 500)
screen = pygame.display.set_mode(screen_dimens)
# }}}

# maze setup {{{
maze = Maze()
maze.load("BinaryTree_8x8.maze")

# }}}

PADDING = 10
CELL_WIDTH = (screen_dimens[0] - PADDING / 2) // maze.num_columns

# main
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(colors["BLACK"])

    walls = []
    for i in range(maze.num_rows):
        for j in range(maze.num_columns):

            # top left corner coordinate
            x1 = (PADDING / 2) + (j * CELL_WIDTH)
            y1 = (PADDING / 2) + (i * CELL_WIDTH)

            # bottom right corner coordinate
            x2 = (PADDING / 2) + ((j + 1) * CELL_WIDTH)
            y2 = (PADDING / 2) + ((i + 1) * CELL_WIDTH)

            if maze.grid[i][j].neighbors["N"] == INF:
                walls.append(Wall(screen, (x1, y1), (x2, y1)))
            if maze.grid[i][j].neighbors["S"] == INF:
                walls.append(Wall(screen, (x1, y2), (x2, y2)))
            if maze.grid[i][j].neighbors["W"] == INF:
                walls.append(Wall(screen, (x1, y1), (x1, y2)))
            if maze.grid[i][j].neighbors["E"] == INF:
                walls.append(Wall(screen, (x2, y1), (x2, y2)))

    # render all walls
    for wall in walls:
        wall.draw()

    pygame.display.flip()

pygame.quit()
