import configparser
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir) 

config = configparser.ConfigParser()
config.read('../doc/settings.ini')
addr = config['socket']['addr']
port = config['socket']['port']
print(addr)

