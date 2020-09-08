import configparser
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
from database import *
from lib.logwriter import *
from lib.iniparser import *
import pandas as pd

class ConnDB_base:
    def __init__(self, url):
        self.db_agent = Database_connection(url)
        # metadata = create_all(self.db_agent)

    def insertToframe(self, df, tablename):
        df.to_sql(tablename, con=self.db_agent,if_exists='append')

    def showTable(self):
        sql = "SELECT * FROM TEST"
        df = pd.read_sql(sql, con=self.db_agent.engine)
        print(df)

if __name__ == '__main__':
    db = ConnDB_base(db_url)
    db.showTable()

