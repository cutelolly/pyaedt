import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pyaedt.common_rpc import launch_server

if int(sys.argv[2]) == 1:
    val = True
else:
    val = False

launch_server(ansysem_path=sys.argv[1], non_graphical=val, port=int(sys.argv[3]))
