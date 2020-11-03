# imports {{{
import sys
import pygame

from Wall import Wall
from Agent import Agent
from Utils import position
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

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

PADDING = 0
CELL_WIDTH = (screen_dimens[0] - PADDING / 2) // maze.num_columns

# initialize player {{{
player_position = (PADDING + 32, PADDING + 32)
player_width = CELL_WIDTH - 10
player_color = colors["RED"]
player_speed = 0.3

PLAYER = Agent(screen, player_position, player_width, player_color, player_speed)
# }}}

# initialize walls {{{
WALLS = []
for i in range(maze.num_rows):
    for j in range(maze.num_columns):

        # top left corner coordinate
        x1 = (PADDING / 2) + (j * CELL_WIDTH)
        y1 = (PADDING / 2) + (i * CELL_WIDTH)

        # bottom right corner coordinate
        x2 = (PADDING / 2) + ((j + 1) * CELL_WIDTH)
        y2 = (PADDING / 2) + ((i + 1) * CELL_WIDTH)

        if maze.grid[i][j].neighbors["N"] == INF:
            WALLS.append(Wall(screen, (x1, y1), (x2, y1)))
        if maze.grid[i][j].neighbors["S"] == INF:
            WALLS.append(Wall(screen, (x1, y2), (x2, y2)))
        if maze.grid[i][j].neighbors["W"] == INF:
            WALLS.append(Wall(screen, (x1, y1), (x1, y2)))
        if maze.grid[i][j].neighbors["E"] == INF:
            WALLS.append(Wall(screen, (x2, y1), (x2, y2)))
# }}}

# render all entities {{{
def redraw():
    screen.fill(colors["BLACK"])

    # draw all WALLS
    for wall in WALLS:
        wall.draw()

    # draw PLAYER
    PLAYER.draw()

    pygame.display.flip()


# }}}

# main
run = True
while run:

    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False

    # sustained keypress actions
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        PLAYER.move_up(WALLS)
    if keys[K_DOWN]:
        PLAYER.move_down(WALLS)
    if keys[K_RIGHT]:
        PLAYER.move_right(WALLS)
    if keys[K_LEFT]:
        PLAYER.move_left(WALLS)

    redraw()
    # print(position((PLAYER.x, PLAYER.y), CELL_WIDTH))


pygame.quit()
