__author__ = 'rrmerugu'

import os, sys
from .config import RSQ_PROJECTS_HOME, RSQ_HOME, RSQ_DB_PATH, RSQ_PROJECTS_CONFIG

if not os.path.exists(RSQ_PROJECTS_HOME):
    os.mkdir(RSQ_PROJECTS_HOME,0755)

if not os.path.exists(RSQ_HOME):
    os.mkdir(RSQ_HOME,0755)

if not os.path.exists(RSQ_PROJECTS_CONFIG): # not very much needed
    os.mkdir(RSQ_PROJECTS_CONFIG, 0755)

if not sys.version_info[:2] == (2, 7):
    print ("Sorry! This tool works only with python version 2.7.")
    exit()
