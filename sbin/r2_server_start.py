__author__ = 'rrmerugu'
"""
This module starts the server that can be accessed at http://localhost:9090.
This server contains the websuite package
"""
import os, sys

"""
Path appended of rsquarelabs_core to sys for accessing modules inside rsquarelabs_core
"""
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)
from rsquarelabs_core.websuite.server import server_run

# server_start()
server_run()