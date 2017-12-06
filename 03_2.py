import sys
from ipdb import launch_ipdb_on_exception, set_trace
from pprint import pprint

input = int(sys.argv[1])

grid = {'0_0': 1}
x_move = True
x_move_max = y_move_max = 1
y_move_left = 0
x_move_left = 1
x_pos = y_pos = 0
cur_value = 1

def collect_adjacent_values(g, x, y):
    return sum([
        g.get('{}_{}'.format(x, y-1), 0),
        g.get('{}_{}'.format(x+1, y-1), 0),
        g.get('{}_{}'.format(x+1, y), 0),
        g.get('{}_{}'.format(x+1, y+1), 0),
        g.get('{}_{}'.format(x, y+1), 0),
        g.get('{}_{}'.format(x-1, y+1), 0),
        g.get('{}_{}'.format(x-1, y), 0),
        g.get('{}_{}'.format(x-1, y-1), 0),
    ])

state = [
   { # X axis
       'move_max': 1,
       'move_left': 0,
       'step_amt': 1,
       'pos': 1,
   }, { # Y axis
       'move_max': 1,
       'move_left': 0,
       'step_amt': 1,
       'pos': 0,
   }
]
active_state = 0
while cur_value < input:
    key = '{}_{}'.format(state[0]['pos'], state[1]['pos'])
    value = collect_adjacent_values(grid, state[0]['pos'], state[1]['pos']) 
    grid[key] = value

    if value > input:
        print(value)
        break

    s = state[active_state]
    if s['move_left'] > 0:
        s['pos'] += s['step_amt']
        s['move_left'] -= 1
    else:
        active_state = abs(active_state - 1)
        s['move_max'] += 1
        s['step_amt'] *= -1 # flip positive/negative step amt
        state[active_state]['move_left'] = state[active_state]['move_max']
        state[active_state]['pos'] += state[active_state]['step_amt']
        state[active_state]['move_left'] -= 1


   # if x_move:
   #     if x_move_left == 0:
   #         x_move_max += 1
   #         x_pos = abs(x_pos)
   #         x_move = False
   #         y_move_left = y_move_max
   #         y_pos -= 1
   #         y_move_left -= 1
   #     else:
   #         x_pos -= 1
   #         x_move_left -= 1
#
   # else:
   #     if y_move_left == 0:
   #         y_move_max += 1
   #         y_pos = abs(y_pos)
   #         x_move = True
   #         x_move_left = x_move_max
   #         x_pos -= 1
   #         x_move_left -= 1
   #     else:
   #         y_pos -= 1
   #         y_move_left -= 1
#print('{}'.format(abs(x_pos) + abs(y_pos)))
