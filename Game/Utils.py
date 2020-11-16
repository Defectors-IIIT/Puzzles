import math

# return manhattan distance between two coordinates
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# return cell position given coordinates
def position(coordinates, cell_width):
    x, y = coordinates
    return (math.ceil(x / cell_width) - 1, math.ceil(y / cell_width) - 1)


# return coordinates of center given cell position
def coordinates(position, cell_width):
    x, y = position
    return (cell_width * (x + 0.5), cell_width * (y + 0.5))
