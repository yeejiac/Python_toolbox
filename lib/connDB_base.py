import configparser
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
from database import *
from lib.logwriter import *
import pandas as pd

class ConnDB_base:
    def __init__(self, url):
        self.db_helper = Database_connection(url)

    def insertToframe(self, df, tablename):
        df.to_sql(tablename, con=self.db_helper,if_exists='append')

