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

db_url = 'mysql://root:Aa1234@localhost:3306/my_db?charset=utf8'
db_weather = 'mysql://root:Aa1234@localhost:3306/weather_data?charset=utf8'

smtp_server = config['gmail_sending']['smtp_server']
mail_port = config['gmail_sending']['port']
mail_addr = config['gmail_sending']['sender_email']
mail_password = config['gmail_sending']['password']






