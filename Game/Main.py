# imports {{{
import sys
import pygame
import random

from Wall import Wall
from Agent import Agent
from Utils import position, coordinates
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

CELL_WIDTH = (screen_dimens[0] - 2) // maze.num_columns

# initialize player {{{
player_position = coordinates((0, 0), CELL_WIDTH)
player_width = CELL_WIDTH // 1.25
player_color = colors["RED"]
player_speed = 0.3

PLAYER = Agent(screen, player_position, player_width, player_color, player_speed, player=True)
# }}}

# initialize walls {{{
WALLS = []
for i in range(maze.num_rows):
    for j in range(maze.num_columns):

        # top left corner coordinate
        x1 = j * CELL_WIDTH
        y1 = i * CELL_WIDTH

        # bottom right corner coordinate
        x2 = (j + 1) * CELL_WIDTH
        y2 = (i + 1) * CELL_WIDTH

        if maze.grid[i][j].neighbors["N"] == INF:
            WALLS.append(Wall(screen, (x1, y1), (x2, y1)))
        if maze.grid[i][j].neighbors["S"] == INF:
            WALLS.append(Wall(screen, (x1, y2), (x2, y2)))
        if maze.grid[i][j].neighbors["W"] == INF:
            WALLS.append(Wall(screen, (x1, y1), (x1, y2)))
        if maze.grid[i][j].neighbors["E"] == INF:
            WALLS.append(Wall(screen, (x2, y1), (x2, y2)))
# }}}

# initialize enemies {{{
enemy1_position = coordinates(
    (random.randint(0, maze.num_rows - 1), random.randint(0, maze.num_columns - 1)), CELL_WIDTH
)
enemy1_width = CELL_WIDTH // 1.25
enemy1_color = colors["BLUE"]
enemy1_speed = 0.3

ENEMY1 = Agent(screen, enemy1_position, enemy1_width, enemy1_color, enemy1_speed)

# }}}

# render all entities {{{
def redraw():
    screen.fill(colors["BLACK"])

    # draw all walls
    for wall in WALLS:
        wall.draw()

    # draw player
    PLAYER.draw()

    # draw enemies
    ENEMY1.draw()

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
