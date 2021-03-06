__author__ = 'rrmerugu'
import os

USER_HOME_FOLDER = os.getenv('HOME')
RSQ_PROJECTS_HOME = os.path.join(USER_HOME_FOLDER, 'rsquarelabsProjects')
RSQ_PROJECTS_CONFIG = os.path.join(RSQ_PROJECTS_HOME, '.config.json') # not very much needed
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
RSQ_LOG_PATH = os.path.join(RSQ_HOME, 'rsquarelabs.log')

RSQ_DB_PATH = os.path.join(RSQ_HOME, 'rsquarelabs.db')
RSQ_DB_LOG = os.path.join(RSQ_HOME, 'DBEngine.log')