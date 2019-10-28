def simple_search(x, y, matrix):
    if matrix[y][x] == 2:
        print('Exit found at %d,%d' % (x, y))
        print("\n")
        for row in matrix:
            print(*row)
        return True
    elif matrix[y][x] == 1:
        print('Wall at %d,%d' % (x, y))
        return False
    elif matrix[y][x] == 3:
        print('Visited %d,%d' % (x, y))
        return False

    print('Visiting %d,%d' % (x, y))

    # Mark visited cell
    matrix[y][x] = 3

    # Search in a clockwise fashion starting with position immediately right of starting point
    if ((x < len(matrix) - 1 and simple_search(x + 1, y, matrix))
            or (y > 0 and simple_search(x, y - 1, matrix))
            or (x > 0 and simple_search(x - 1, y, matrix))
            or (y < len(matrix) - 1 and simple_search(x, y + 1, matrix))):
        return True

    return False


def solve_maze(maze, strategy):
    print("\n")
    print('A maze is shown below.',
          'Open cells are shown as 0, walls as 1, exits as 2 and visited cells as 3.')
    print("\n")
    # Ensure maze appears in matrix format in terminal
    for row in maze:
        print(*row)
    print("\n")
    # Ensure starting coordinates are reachable
    while True:
        try:
            start_x_position = int(input("Enter starting x-coordinate: "))
            start_y_position = int(input("Enter starting y-coordinate: "))
            print("\n")
            strategy(start_x_position, start_y_position, maze)
            print("\n")
            break
        except ValueError:
            print('Coordinates must be integers!')
        except IndexError:
            print('Coordinates of start position must exist in the maze.')
