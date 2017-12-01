import sys
import ipdb

data = sys.stdin.read().replace("\n", '')
sys.stdin = open('/dev/tty')
matches = []

for i in range(0, len(data) - 1):
    if data[i] == data[i+1]:
        matches.append(data[i])

if data[-1] == data[0]:
    matches.append(data[-1])

print('{}'.format(sum(map(int, matches))))

