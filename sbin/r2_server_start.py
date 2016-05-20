__author__ = 'rrmerugu'
import os, sys

"""
adds the rsquarelabs-core module to this script path to access the modules inside rsquarelabs-core
"""
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)

from rsquarelabs_core.websuite.server import server_run
"""
Runs the server
"""
server_run()