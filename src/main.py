
maze = [[1, 2, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]]


def simple_search(x, y, matrix):
    if matrix[x][y] == 2:
        print('Exit found at %d,%d' % (x, y))
        return True
    elif matrix[x][y] == 1:
        print('Wall at %d,%d' % (x, y))
        return False
    elif matrix[x][y] == 3:
        print('Visited %d,%d' % (x, y))
        return False

    print('Visiting %d,%d' % (x, y))

    # Mark visited cell
    matrix[x][y] = 3

    # Search in a clockwise fashion starting with position immediately right of starting point
    if ((x < len(matrix) - 1 and simple_search(x + 1, y, matrix))
        or (y > 0 and simple_search(x, y - 1, matrix))
        or (x > 0 and simple_search(x - 1, y, matrix))
        or (y < len(matrix) - 1 and simple_search(x, y + 1, matrix))):
        return True

    return False


simple_search(1, 4, maze)
