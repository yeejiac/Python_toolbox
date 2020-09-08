import configparser
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
import psycopg2

config = configparser.ConfigParser()
config.read('../doc/settings.ini')
addr = config['socket']['addr']
port = int(config['socket']['port'])



# maxdb = psycopg2.connect(
#   user=config['database']['user'],
#     password=config['database']['password'],
#     host=config['database']['addr'],
#     port=int(config['database']['port']),
#     database=config['database']['database'],
#   )
# cursor=maxdb.cursor()

db_url = 'mysql://root:Aa1234@localhost:3306/my_db'




