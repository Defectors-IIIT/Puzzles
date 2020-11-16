import sys
import random
from Utils import position

sys.path.append("../")
from Core.maze import INF


def RandomWalk(agent, STATE):
    x, y = position(agent.rect.center, STATE["cell_width"])
    cell = STATE["maze"].grid[y][x]
    choices = [k for k, v in cell.neighbors.items() if v != INF]
    return random.choice(choices)
