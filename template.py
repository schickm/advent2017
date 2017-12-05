import sys
from ipdb import launch_ipdb_on_exception

input = sys.argv[1]

with launch_ipdb_on_exception():
    pass
