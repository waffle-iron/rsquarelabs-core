__author__ = 'rrmerugu'

import os, sys
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)
from rsquarelabs_core.websuite.rmv import server_run

# server_start()
server_run()