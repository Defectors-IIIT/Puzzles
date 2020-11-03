import random
from Utils import position, coordinates


def random_walk(agent, STATE):
    y, x = position(agent.rect.center, STATE["cell_width"])
    cell = STATE["maze"].grid[x][y]
    choices = [k for k, v in cell.neighbors.items() if v == 0]
    return random.choice(choices)
