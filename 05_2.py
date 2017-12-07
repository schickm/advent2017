import sys
from ipdb import launch_ipdb_on_exception, set_trace
from pprint import pprint
input = sys.argv[1]

with open(input) as f:
    maze = [int(x) for x in f.read().split('\n')]
    steps = 0
    index = 0
    try:
        while True:
            val = maze[index]

            if val >= 3:
                adjustment = -1
            else:
                adjustment = 1
            maze[index] += adjustment

            index += val
            steps += 1
    except IndexError:
        print(steps)
