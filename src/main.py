
maze = [[1, 2, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]]


def simple_search(x, y, matrix):
    if matrix[y][x] == 2:
        print('Exit found at %d,%d' % (x, y))
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

print("\n")
print('A maze is shown below.', \
      'Open cells are denoted by 0, walls by 1 and exits by 2.')
print("\n")

for row in maze:
    print(*row)

print("\n")
start_x_position = int(input ("Enter starting x-coordinate: "))
start_y_position = int(input ("Enter starting y-coordinate: "))
print("\n")

simple_search(start_x_position, start_y_position, maze)
print('Complete!')
