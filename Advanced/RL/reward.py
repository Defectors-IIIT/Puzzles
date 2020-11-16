from helper import state_to_cell

def reward_cell(maze, cell):
    """
    takes input as current cell.

    returns 0 if cell is the end state, else -1
    """

    if cell[0] == maze.num_rows - 1 and cell[1] == maze.num_columns - 1:
        return 0
    else:
        return -1

def reward(maze, state):
    """
    takes input as current state.
    uses reward(cell)
    returns 0 if cell is the end state, else -1
    """
    return reward_cell(maze, state_to_cell(maze, state))
