import sys
from ipdb import launch_ipdb_on_exception
from pprint import pprint

input = int(sys.argv[1])

with launch_ipdb_on_exception():
    grid = {}
    x_move_max = 1
    y_move_max = 1
    x_pos = 0
    y_pos = 0
    location = 1
    for location in range(1, input + 1):
        grid[location] = (x_pos, y_pos)
        print('{} = {}, {}'.format(location, x_pos, y_pos))
        x_pos += 1
        y_pos += 1

        if x_pos == x_move_max:
            x_move_max += 1
        if y_pos == y_move_max:
            y_move_max += 1

    pprint(grid)
