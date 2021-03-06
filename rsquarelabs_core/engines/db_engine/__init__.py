import sqlite3, os, logging
from rsquarelabs_core.config import  RSQ_DB_LOG, RSQ_DB_PATH

"""
db_engine is a module built as database handler across the project.
db_engine uses sqlite as the database .


"""


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler(RSQ_DB_LOG)
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)


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
            logger.debug(e)
            pass

        self.cur = self.conn.cursor()
        return self.conn

    def do_select(self, cmd):

        data = self.cur.execute(cmd)
        return data

    def do_insert(self, cmd):
        try:
            self.cur.execute(cmd)
            self.conn.commit()
        except Exception as e:
            logger.error(e)
            logger.error(e.message)
        return self.cur

