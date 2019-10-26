import numpy as np
import random

# Set matrix dimensions
n = 6
m = 5

# Initialise matrix
matrix = np.ones((n, m), dtype=int)

# Initialise start point away from edge
start_x_position = random.randrange(1, n-1)
start_y_position = random.randrange(1, m-1)
start_position = (start_x_position, start_y_position)
matrix[start_position] = 2

def create_escape_path(x_position, y_position):
    