import sys
from ipdb import launch_ipdb_on_exception
from pprint import pprint

input = int(sys.argv[1])

grid = {}
x_move = True
x_move_max = y_move_max = 1
y_move_left = 0
x_move_left = 1
x_pos = y_pos = 0
location = 1

for location in range(1, input + 1):
    grid[location] = (abs(x_pos), abs(y_pos))

    if x_move:
        if x_move_left == 0:
            x_move_max += 1
            x_pos = abs(x_pos)
            x_move = False
            y_move_left = y_move_max
            y_pos -= 1
            y_move_left -= 1
        else:
            x_pos -= 1
            x_move_left -= 1
    else:
        if y_move_left == 0:
            y_move_max += 1
            y_pos = abs(y_pos)
            x_move = True
            x_move_left = x_move_max
            x_pos -= 1
            x_move_left -= 1
        else:
            y_pos -= 1
            y_move_left -= 1
pprint(grid)
#print('{}'.format(abs(x_pos) + abs(y_pos)))
