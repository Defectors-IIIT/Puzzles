import sys

sys.path.append("../")
sys.path.append("../../")

from pprint import pprint
from Core.maze import Maze, INF

import random

import policy
from reward import reward
from helper import get_next_state, get_valid_actions

# rate of learning
LEARNING_RATE = 0.1

# discounting future rewards from Q value
DISCOUNT = 0.90

# set of all actions that can be taken
# N, S, W, E
ACTIONS = [0, 1, 2, 3]

N = M = 4

def load_maze():
    global maze 
    maze = Maze()
    maze.load(f"BinaryTree_{N}x{N}.maze")
    # display(maze.draw(cell_width=40))

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

def execute_episode():
    # iterate through all the states
    for state in range(N*N):
        action = policy.greedy(state, ACTIONS, Q)
        q_table[state][action] += LEARNING_RATE * (
            reward(maze, state)
            + DISCOUNT * max([
                Q(get_next_state(maze, state, next_action), next_action) 
                for next_action in get_valid_actions(maze, state, ACTIONS) 
            ])
            - Q(state, action)
        )
