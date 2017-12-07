import sys
from ipdb import launch_ipdb_on_exception, set_trace
from pprint import pprint

input = sys.argv[1]

with open(input) as f:
    past_allocations = {}
    banks = [int(x) for x in f.read().rstrip().split('\t')]
    cycles = 0
    prev_cycle = None

    while True:
        key = '_'.join([str(x) for x in banks])
        if past_allocations.get(key, None):
            prev_cycle = past_allocations.get(key)
            break

        past_allocations[key] = cycles
        blocks = max(banks)
        index = banks.index(max(banks))
        banks[index] = 0

        while blocks > 0:
            index += 1
            if index == len(banks):
                index = 0
            banks[index] += 1
            blocks -= 1

        cycles += 1

    pprint(cycles - prev_cycle)
