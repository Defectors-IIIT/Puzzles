from helper import state_to_cell, get_next_state
from mirage_helper import check

INF = float('inf')
ACTION_MAPPER = {
        0: 'N',
        1: 'S',
        2: 'W',
        3: 'E'
    }

def reward(maze, state, action):
    next_state = get_next_state(maze, state, action)
    x, y = state_to_cell(maze, state)

    if maze.grid[x][y].neighbors[ACTION_MAPPER[action]] == INF:
        return -10000
    elif next_state == (maze.num_rows*maze.num_columns - 1):
        return 1000
    else:
        return 0

def reward_mirage(maze, mirage, state, action):
    if action >= 4:
        x, y = state_to_cell(maze, state)
        direction = ACTION_MAPPER[action-4]
        if check(mirage, maze, x, y, direction):
            return 100
        else:
            return -100
    else:
        return reward(maze, state, action)
