import sqlite3, os, logging

"""
This module contains methods to create a database, connect to the same and access it.
"""

"""
Readable (str) describing the path to current user's HOME directory.
Example: /home/nitish
"""
USER_HOME_FOLDER = os.getenv('HOME')

"""
Readable (str) describing the path to created directory 'rsquarelabsProjects' in current user's HOME.
All the projects created by user will be saved in this path.
Example: /home/nitish/rsquarelabsProjects
"""
RSQ_PROJECTS_HOME = os.path.join(USER_HOME_FOLDER, 'rsquarelabsProjects')

"""
Readable (str) describing the path to created directory '.rsquarelabs' in current user's HOME
Created database and database's log-file will be saved int this path
Example: /home/nitish/.rsquarelabs
"""
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')

"""
Readable (str) describing the path to created database 'rsquarelabs.db' in '.rsquarelabs'
Project data will be saved in this path
Example: /home/nitish/.rsquarelabs/rsquarelabs.db
"""
RSQ_DB_PATH = os.path.join(RSQ_HOME, 'rsquarelabs.db')

"""
Readable (str) describing the path to created log-file 'DBEngine.log' in '.rsquarelabs'
Records the every executed method in this path
Example: /home/nitish/.rsquarelabs/DBEngine.log
"""
RSQ_DB_LOG = os.path.join(RSQ_HOME, 'DBEngine.log')

"""
Logging this module database
All the log-strings saved to DBEngine.log
Example: We can use logging.info(), logging.debug() other methods like warning() for recording the events.
"""
logging.basicConfig(filename=RSQ_DB_LOG, level=logging.DEBUG)

class DBEngine:
    """
    This class is a custom written for database transactions
    """
    def __init__(self, db_name):
        """
        This method takes db_name as argument and calls do_connect method.

        :param db_name:(str) name of the database
        """
        logging.debug('This msg should go to log file')
        logging.info('init is running')
        self.do_connect(db_name)

    def do_connect(self, db_name):
        """
        This method connects the database using sqlite3, creates the database using tables.sqlite
        and sets the cursor object.

        :param db_name:(str) name of the database
        :return: returns the connection object
        """
        self.conn = sqlite3.connect(db_name)
        sql_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables.sqlite')
        tables_structure = open(sql_file_path).read()
        try:
            # TODO - Need improvements
            self.conn.execute(tables_structure)
        except Exception as e:
            #print e
            pass

        self.cur = self.conn.cursor()
        return self.conn

    def do_select(self, cmd):
        """
        This method selects the data from the database using cursor object and executing command (cmd) as argument.

        :param cmd: (str) command to be executed
        :return: returns (list) the data of objects which is selected
        """
        cursor = self.cur.execute(cmd)
        return cursor

    def do_insert(self, cmd):
        """
        This method inserts the data into the database using cursor object and executing command (cmd) as argument.
        And saving the insertion by committing the connection object

        :param cmd: (str) command to be executed
        :return: returns the cursor object
        """
        self.cur.execute(cmd)
        self.conn.commit()
        return self.cur