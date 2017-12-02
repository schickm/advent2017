import sys

row_diffs = []

with open(sys.argv[1]) as f:
    for line in f:
        values = list(map(int, line.rstrip().split('\t')))
        min = max = values[0]
        for v in values[1:]:
            if v < min:
                min = v
            if v > max:
                max = v

        row_diffs.append(max - min)

print('{}'.format(sum(row_diffs)))
