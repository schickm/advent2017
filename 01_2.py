import sys
import ipdb

data = sys.stdin.read().replace("\n", '')
sys.stdin = open('/dev/tty')
matches = []

total_length = len(data)
len_ahead = int(total_length / 2)

def get_next(index):
    next_index = index + len_ahead
    overage = next_index - total_length
    if overage > -1:
        next_index = overage

    return data[next_index]


for i in range(0, len(data)):
    if data[i] == get_next(i):
        matches.append(data[i])

print('{}'.format(sum(map(int, matches))))

