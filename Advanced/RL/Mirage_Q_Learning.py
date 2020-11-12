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

from Q_Learning import load_maze, reset_q_table, print_q_table, visualise_q_table, Q
from mirage_helper import Mirage, check

N = M = 8
ACTIONS = [0, 1, 2, 3, 4]
DISCOUNT = 0.8
LEARNING_RATE = 0.5

def execute_episode():
    for state in range(N*M):
        action = e_greedy(
            state, 
            get_valid_actions(maze, state, ACTIONS), 
            Q, epsilon=0.1)
        R = reward_mirage(maze, mirage_maze state, action)
        next_state = get_next_state(maze, state, action)
        
        next_best = max(q_table[next_state])
        
        td_target = R + DISCOUNT * next_best
        td_diff = td_target - q_table[state][action]
        
        q_table[state][action] += LEARNING_RATE * td_diff        
        q_table[state][action] = round(q_table[state][action], 3)

if __name__ == "__main__":
    load_maze()
    global mirage_maze
    mirage_maze = Mirage(maze, 0.2)

    reset_q_table()
    for _ in range(100):
        execute_episode()
    
    print_q_table()
    visualise_q_table()
