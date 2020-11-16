import sys
from Utils import position, manhattan
from heapq import heappush, heappop

sys.path.append("../")
from Core.maze import INF


def Heuristic(a, b):
    # The heurisitc used is Manhattan distance since only 4 directions are possible from a particular point
    return manhattan(a,b)


def AStar(agent, STATE):
    maze = STATE["maze"]
    sy, sx = position(agent.rect.center, STATE["cell_width"])
    start = (sx, sy)
    gy, gx = position(STATE["player"].rect.center, STATE["cell_width"])
    goal = (gx, gy)

    # Declarations
    neighbors = [(1, 0, "S"), (-1, 0, "N"), (0, 1, "E"), (0, -1, "W")]
    visited = set()
    cameFrom = {}
    gScore = {start: 0}
    fScore = {start: Heuristic(start, goal)}
    priorityQ = []

    # Initialising the proprity queue with the start node and its f score
    heappush(priorityQ, (fScore[start], start))
    # Looping till the priority queue is empty
    while priorityQ:
        current = heappop(priorityQ)[1]
        # Stops and returns the path if the current node is the target node
        if current == goal:
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path = path + [start]
            path = path[::-1]
            if len(path) > 1:
                next_cell = path[1]
                xd = start[1] - next_cell[1]
                yd = start[0] - next_cell[0]
                if xd == 0 and yd == 0:
                    return False
                else:
                    if xd < 0:
                        return "E"
                    elif xd > 0:
                        return "W"
                    elif yd < 0:
                        return "S"
                    elif yd > 0:
                        return "N"

            # return path

        # Marking current node as visited
        visited.add(current)

        for i, j, k in neighbors:
            neighbor = (current[0] + i, current[1] + j)
            # Checking if the neighbor is out of bounds or if the path to the neighbor is blocked
            if neighbor[0] < 0 or neighbor[0] >= len(maze.grid[0]):
                continue
            if neighbor[1] < 0 or neighbor[1] >= len(maze.grid):
                continue
            if maze.grid[current[0]][current[1]].neighbors[k] == INF:
                continue
            # Calculating g and f scores
            tentative_gScore = gScore[current] + maze.grid[current[0]][current[1]].neighbors[k]
            tentative_fScore = tentative_gScore + Heuristic(neighbor, goal)
            # Checking if the current f score is less than or equal to the calculated one
            if neighbor in visited and tentative_fScore >= fScore.get(neighbor, INF):
                continue
            # Checking if the current f score is greater than the calculated one
            if tentative_fScore < fScore.get(neighbor, INF):
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_fScore
                heappush(priorityQ, (fScore[neighbor], neighbor))
    return False  # Path does not exist
