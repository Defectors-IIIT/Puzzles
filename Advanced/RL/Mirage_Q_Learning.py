import sys

sys.path.append("../")
sys.path.append("../../")

from pprint import pprint
from Core.maze import Maze, INF

import random
import numpy as np

from helper import get_next_state, get_valid_actions
from policy import e_greedy
from reward import reward_mirage

from mirage_helper import Mirage

N = M = 8
ACTIONS = [i for i in range(8)]
DISCOUNT = 0.8
LEARNING_RATE = 0.5
ACTION_MAPPER = {
        0: 'N',
        1: 'S',
        2: 'W',
        3: 'E'
    }

def load_maze():
    global maze 
    maze = Maze()
    maze.load(f"BinaryTree_{N}x{M}.maze")

def reset_q_table():
    """
    initialises/resets the q table
    """
    # setup the q table
    global q_table
    q_table = []

    for i in range(N):
        for j in range(M):
            temp = []
            for value in maze.grid[i][j].neighbors.values():
                if value == INF:
                    # we HIGHLY discourage going through of walls
                    temp.append(-1000)
                else:
                    # we favor exploration for unseen states
                    # NOTE the use of states. 
                    # We dont want to be exploring all the actions, 
                    # but all the states 
                    temp.append(10)
            
            # decision to chech for mirage wall is neutral
            for _ in range(4):
                temp.append(0)
            
            # temp now has the values for ONE state.
            q_table.append(temp)

def print_q_table():
    for i in range(N*M):
        print(q_table[i], end="\t")
        if not (i+1) % N:
            print()

def visualise_q_table():
    for i in range(N*M):
        try:
            print(ACTION_MAPPER[np.argmax(q_table[i])], end="\t")
        except:
            print('F', end="\t")
        if not (i+1) % N:
            print()

def Q(state, action):
    return q_table[state][action]

def execute_episode():
    for state in range(N*M):
        action = e_greedy(
            state, 
            get_valid_actions(maze, state, ACTIONS), 
            Q, epsilon=0.1)
        R = reward_mirage(maze, mirage, state, action)
        next_state = get_next_state(maze, state, action)
        
        next_best = max(q_table[next_state])
        
        td_target = R + DISCOUNT * next_best
        td_diff = td_target - q_table[state][action]
        
        q_table[state][action] += LEARNING_RATE * td_diff        
        q_table[state][action] = round(q_table[state][action], 3)

if __name__ == "__main__":
    load_maze()
    global mirage
    mirage = Mirage(maze, 0.2)

    reset_q_table()
    for _ in range(512):
        execute_episode()
    
    print_q_table()
    visualise_q_table()
