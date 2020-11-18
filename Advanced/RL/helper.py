def state_to_cell(maze, state):
    """
    input:
        state:
            the mapping to the linearised q-table index
    return:
        cell:
            tuple of indices
    """
    if not (0 <= state < maze.num_rows*maze.num_columns):
        return None
    quotient = state//maze.num_rows
    remainder = state - quotient * maze.num_rows
    return (quotient, remainder)

def cell_to_state(maze, cell):
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

def in_range(maze, x, y):
    if not (0 <= x < maze.num_rows):
        return False
    if not (0 <= y < maze.num_columns):
        return False
    return True

def get_next_cell(maze, current_cell, action):
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
    
    if not in_range(maze, x, y):
        return None
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dx, dy = directions[action]

    if not in_range(maze, x+dx, y+dy):
        return None

    return (x+dx, y+dy)

def get_next_state(maze, state, action):
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
    start_cell = state_to_cell(maze, state)
    end_cell = get_next_cell(maze, start_cell, action)
    try:
        return cell_to_state(maze, end_cell)
    except:
        return None

def get_valid_actions(maze, state, ACTIONS):
    valid_actions = []
    for action in ACTIONS:
        if get_next_state(maze, state, action):
            valid_actions.append(action)
    return valid_actions
