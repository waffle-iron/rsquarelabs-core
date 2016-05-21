import sqlite3, os, logging
# from rsquarelabs_core.config import  RSQ_DB_LOG
from rsquarelabs_core.config import  RSQ_DB_LOG, RSQ_DB_PATH

"""
db_engine is a module built as database handler across the project.
db_engine uses sqlite as the database .


"""


logging.basicConfig(filename=RSQ_DB_LOG, level=logging.DEBUG)

class DBEngine:

    def __init__(self, db_name):
        self.do_connect(db_name)

    def do_connect(self, db_name):
        self.conn = sqlite3.connect(db_name)
        sql_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.sql')
        tables_structure = open(sql_file_path).read()

        try:
            self.conn.executescript(tables_structure)
        except Exception as e:
            logging.debug(e)
            pass

        self.cur = self.conn.cursor()
        return self.conn

    def do_select(self, cmd):
        data = self.cur.execute(cmd)
        return data

    def do_insert(self, cmd):
        self.cur.execute(cmd)
        self.conn.commit()
        return self.cur