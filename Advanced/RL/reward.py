from helper import state_to_cell
from mirage_helper import check
from Q_Learning import ACTION_MAPPER

def reward(maze, state):
    return 1000 if state == (maze.num_rows*maze.num_columns - 1) else 0

def reward_mirage(maze, mirage, state, action):
    if action == 4:
        x, y = state_to_cell(state)
        direction = ACTION_MAPPER[action]
        if check(mirage, maze, x, y, direction):
            return 100
        else:
            return -100
    else:
        return reward(maze, state)
