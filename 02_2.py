import sys
from ipdb import launch_ipdb_on_exception

row_diffs = []

with launch_ipdb_on_exception():
    with open(sys.argv[1]) as f:
        for line in f:
            values = list(map(int, line.rstrip().split('\t')))

            for i in range(0, len(values)):
                diff = None
                for j in range(0, len(values)):
                    if values[i] ==values[j]:
                        continue
                    if values[i] %values[j] == 0:
                        diff = int(values[i] /values[j])
                        break

                if diff:
                    row_diffs.append(diff)
                    break


    print('{}'.format(sum(row_diffs)))
