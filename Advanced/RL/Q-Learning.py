import sys

sys.path.append("../")
sys.path.append("../../")

from pprint import pprint
from Core.maze import Maze, INF

import random

# rate of learning
LEARNING_RATE = 0.1

# discounting future rewards from Q value
DISCOUNT = 0.90

# set of all actions that can be taken
# N, S, W, E
ACTIONS = [0, 1, 2, 3]

def load_maze(N=4):
    global maze 
    maze = Maze()
    maze.load(f"BinaryTree_{N}x{N}.maze")
    # display(maze.draw(cell_width=40))

def state_to_cell(state):
    """
    input:
        state:
            the mapping to the linearised q-table index
    return:
        cell:
            tuple of indices
    """
    if not (0 <= state < N*N):
        return None
    quotient = state//maze.num_rows
    remainder = state - quotient * maze.num_rows
    return (quotient, remainder)

def cell_to_state(cell):
    """
    input:
        cell:
            tuple of indices
    return:
        state:
            the mapping to the linearised q-table index
    """
    if not (0 <= cell[0] < maze.num_rows and 0 <= cell[1] < maze.num_columns):
        return None
    return cell[0]*maze.num_rows + cell[1]

def reward_cell(cell):
    """
    takes input as current cell.

    returns 0 if cell is the end state, else -1
    """

    if cell[0] == maze.num_rows - 1 and cell[1] == maze.num_columns - 1:
        return 0
    else:
        return -1

def reward(state):
    """
    takes input as current state.
    uses reward(cell)
    returns 0 if cell is the end state, else -1
    """
    return reward_cell(state_to_cell(state))

def in_range(x, y):
    if not (0 <= x < maze.num_rows):
        return False
    if not (0 <= y < maze.num_columns):
        return False
    return True

def get_next_cell(current_cell, action):
    """
    TODO: RESTRICT THE ACTION SPACE TO ACCESS ONLY THE NON-INF EDGES
    input:
        current_state:
            the current tuple of indices in the grid
        action:
            any of [0, 1, 2, 3] 
            taking the directions N, S, W, E respectively

    returns:
        valid action: the index tuple of the next state
        invalid action: None
    """

    if not (0 <= action < 4):
        raise ValueError(f"Invalid action {action}. Must be in [0, 3] range.")
    
    x, y = current_cell
    
    if not in_range(x, y):
        return None
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dx, dy = directions[action]

    if not in_range(x+dx, y+dy):
        return None

    return (x+dx, y+dy)

def get_next_state(state, action):
    """
    Uses the get_next_cell function. Easie to use due to the helper functions.
    input:
        state: 
            current state
        action:
            current action
    return:
        future state
    """
    start_cell = state_to_cell(state)
    end_cell = get_next_cell(start_cell, action)
    try:
        return cell_to_state(end_cell)
    except:
        return None

def get_valid_actions(state):
    valid_actions = []
    for action in ACTIONS:
        if get_next_state(state, action):
            valid_actions.append(action)
    return valid_actions

def reset_q_table():
    """
    initialises/resets the q table
    """
    # setup the q table
    global q_table
    q_table = []

    for i in range(maze.num_rows):
        for j in range(maze.num_columns):
            temp = []
            for value in maze.grid[i][j].neighbors.values():
                # the edges which are walls have value as -inf, 
                # to discourage any agent trying to go from there
                temp.append(-value)
            q_table.append(temp)

def Q(state, action):
    return q_table[state][action]

def iterate():
    # iterate through all the states
    for i in range(N*N):
        for j in ACTIONS:
            q_table[i][j] += LEARNING_RATE * (
                reward(i)
                + DISCOUNT * max([
                    Q(get_next_state(i, action), action) for action in get_valid_actions(i) 
                ])
                - Q(i, j)
            )

if __name__ == "__main__":
    global N
    N = 4
    load_maze(N)
    
    reset_q_table()

    iterate()

    last_state = N*N-1
    print(q_table[last_state])