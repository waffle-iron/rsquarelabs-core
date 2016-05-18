__author__ = 'rrmerugu'

# simulating the installation thru pip.. ie., adding the rsquarelabs_core to the path
import os, sys
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)
# you can remove/uncomment the above code if you installed rsquarelabs_core thru pip ie.,

###########################################################
# SCENARIO_1 : This is the very basic implementation of opening a webserver and accessing the RMV - RSQUARE MOLECULAR VIEWER
#
#
###########################################################

from rsquarelabs_core.websuite.server import server_start_cmd, server_run
from rsquarelabs_core.utils import brower_open, browser_register



# If you need webserver to start for documentation or anything in the background( for any further purposes)
# server_start_cmd()
server_run()
# Open the page in new tab
brower_open('http://localhost:9090/websuite/index.html')





