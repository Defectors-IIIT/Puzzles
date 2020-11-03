import math

# return cell position given coordinates
def position(coordinates, cell_width):
    x, y = coordinates
    return (math.ceil(x / cell_width) - 1, math.ceil(y / cell_width) - 1)
