import sys
from Utils import position, manhattan,  coordinates
from copy import deepcopy 

sys.path.append("../")
from Core.maze import INF

INF = float('inf')

def evaluation_function(positions):
    # Need a better evaluation function and need a different type of maze. 
    # Potentially - penalize dead ends, have rewards, have game over state
    pos = positions[0]
    targets = positions[1:]
    distance = 0

    for target in targets:
        ghost_dist = manhattan(pos, target)
        if(ghost_dist <= 1):
            ghost_dist = -100
        distance+=ghost_dist

    return distance

# Gets the possible directions that an agent can move to
# given it's current position
def get_possible_directions(agent_index, positions, maze):
    neighbors = [(0, 1, "S"), (0, -1, "N"), (1, 0, "E"), (-1, 0, "W")]
    current = positions[agent_index]
    #print(maze.grid[current[1]][current[0]].neighbors)
    possible_directions = []
    for i, j, k in neighbors:
        neighbor = (current[0] + i, current[1] + j)
        # Checking if the neighbor is out of bounds or if the path to the neighbor is blocked
        if neighbor[0] < 0 or neighbor[0] >= len(maze.grid):
            continue
        if neighbor[1] < 0 or neighbor[1] >= len(maze.grid[0]):
            continue
        if maze.grid[current[1]][current[0]].neighbors[k] == INF:
            continue
        possible_directions.append(k)
    return possible_directions

# Returns the new position of an agent given a direction to move in
def get_new_positions(agent_index, direction, positions):
    neighbors = {"E":(1, 0), "W":(-1, 0), "S":(0, 1), "N":(0, -1)}
    new_positions = deepcopy(positions)
    current = new_positions[agent_index]
    new_pos = (current[0]+neighbors[direction][0], current[1]+neighbors[direction][1])
    new_positions[agent_index] = new_pos

    return new_positions

# Function that is called by agent to get the next move
def Minimax_helper(agent, STATE):
    all_agents = [STATE["player"],]
    all_agents.extend(STATE["enemies"])

    # Array of positions of all the agents. The player agent is index 0
    positions = [position(agent.rect.center, STATE["cell_width"]) for agent in all_agents]
    max_eval = -INF
    final_direction = None
    maze = STATE["maze"]
    possible_directions = get_possible_directions(0, positions, maze)
    #print(possible_directions)
    for direction in possible_directions:
        new_positions = get_new_positions(0, direction, positions)
        ev = minimax(2, True, 1, -INF, INF, new_positions, maze)
        #print(new_positions, direction, ev)
        if(ev > max_eval):
            max_eval = ev
            final_direction = direction
    #print(final_direction)
    return final_direction

def minimax(depth, is_maximizing, agent_index, alpha, beta, positions, maze):
    if(depth == 0):
        return evaluation_function(positions)
    
    possible_directions = get_possible_directions(agent_index, positions, maze)

    if(is_maximizing):
        max_eval = -INF
        for direction in possible_directions:
            new_positions = get_new_positions(agent_index, direction, positions)
            ev = minimax(depth-1, False, 1, alpha, beta, new_positions, maze)
            max_eval = max(max_eval, ev)
            alpha = max(alpha, ev)
            if(alpha >= beta):
                break
        return max_eval
    
    else:
        min_eval = INF
        if(agent_index == len(positions)-1):
            for direction in possible_directions:
                new_positions = get_new_positions(agent_index, direction, positions)
                ev = minimax(depth-1, True, 0, alpha, beta, new_positions, maze)
                min_eval = min(min_eval, ev)
                beta = min(beta, ev)
                if(beta <= alpha):
                    break
            return min_eval
        else:
            for direction in possible_directions:
                new_positions = get_new_positions(agent_index, direction, positions)
                ev = minimax(depth-1, False, agent_index+1, alpha, beta, new_positions, maze)
                if(ev < min_eval):
                    min_eval = ev
            return min_eval


