# imports {{{
import sys
import pygame
import random
import time 

from Wall import Wall
from Agent import Agent
from Utils import position, coordinates

from AStar import AStar
from RandomWalk import RandomWalk
from Minimax import Minimax_helper

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
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "violet": (255, 0, 255),
    "yellow": (255, 255, 0),
}
# }}}

# pygame setup {{{
pygame.display.init()
# pygame.init()

screen_dimens = (500, 500)
screen = pygame.display.set_mode(screen_dimens)
# }}}

# maze setup {{{
maze = Maze()
maze.load("BinaryTree_16x16.maze")
# }}}

# initialize game state {{{
CELL_WIDTH = (screen_dimens[0] - 2) // maze.num_columns

STATE = {
    "cell_width": CELL_WIDTH,
    #"screen": screen,
    "maze": maze,
    "walls": [],
    "enemies": [],
    "player": None,
}
# }}}

# initialize walls {{{
for i in range(maze.num_rows):
    for j in range(maze.num_columns):

        # top left corner coordinate
        x1 = j * CELL_WIDTH
        y1 = i * CELL_WIDTH

        # bottom right corner coordinate
        x2 = (j + 1) * CELL_WIDTH
        y2 = (i + 1) * CELL_WIDTH

        if maze.grid[i][j].neighbors["N"] == INF:
            STATE["walls"].append(Wall(screen, (x1, y1), (x2, y1)))
        if maze.grid[i][j].neighbors["S"] == INF:
            STATE["walls"].append(Wall(screen, (x1, y2), (x2, y2)))
        if maze.grid[i][j].neighbors["W"] == INF:
            STATE["walls"].append(Wall(screen, (x1, y1), (x1, y2)))
        if maze.grid[i][j].neighbors["E"] == INF:
            STATE["walls"].append(Wall(screen, (x2, y1), (x2, y2)))
# }}}

# initialize player {{{
player_position = coordinates((0, 0), CELL_WIDTH)
player_width = CELL_WIDTH // 1.25
player_color = COLORS["red"]
player_speed = 0.3

STATE["player"] = Agent(
    screen, player_position, player_width, player_color, player_speed, player=True
)
# }}}

# initialize enemies {{{
enemy1_position = coordinates(
    (random.randint(0, maze.num_rows - 1), random.randint(0, maze.num_columns - 1)), CELL_WIDTH
)
enemy1_width = CELL_WIDTH // 1.25
enemy1_color = COLORS["blue"]
enemy1_speed = 0.3

STATE["enemies"].append(Agent(screen, enemy1_position, enemy1_width, enemy1_color, enemy1_speed))

enemy2_position = coordinates(
    (random.randint(0, maze.num_rows - 1), random.randint(0, maze.num_columns - 1)), CELL_WIDTH
)
enemy2_width = CELL_WIDTH // 1.25
enemy2_color = COLORS["green"]
enemy2_speed = 0.2

STATE["enemies"].append(Agent(screen, enemy2_position, enemy2_width, enemy2_color, enemy2_speed))
# }}}

# render all entities {{{
def redraw():
    screen.fill(COLORS["black"])

    # draw all walls
    for wall in STATE["walls"]:
        wall.draw()

    # draw enemies
    for enemy in STATE["enemies"]:
        enemy.draw()

    # draw player
    STATE["player"].draw()

    pygame.display.flip()


# }}}
# main
try:
    human_controlled = sys.argv[1]
except:
    human_controlled = False

run = True
while run:

    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False

    # sustained keypress actions
    if(human_controlled):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            STATE["player"].move_up(STATE["walls"])
        if keys[K_DOWN]:
            STATE["player"].move_down(STATE["walls"])
        if keys[K_RIGHT]:
            STATE["player"].move_right(STATE["walls"])
        if keys[K_LEFT]:
            STATE["player"].move_left(STATE["walls"])
    else:
        STATE["player"].walk(Minimax_helper, STATE)

    # entity actions
    STATE["enemies"][0].walk(RandomWalk, STATE)
    STATE["enemies"][1].walk(AStar, STATE)
    redraw()

pygame.quit()
