from functions import *

example_maze = [[1, 2, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1]]

solve_maze(example_maze, simple_search)
