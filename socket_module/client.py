import socket
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
# from lib.iniparser import * 
from lib.logwriter import *
import queue 
import threading
import time


class Client_socket:
    def __init__(self, addr, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((addr, port))
        self.dtaq = queue.Queue(maxsize = 10)
        t_send = threading.Thread(target = self.send())
        t_send.start()
        t_recv = threading.Thread(target = self.recv())
        t_recv.start()
        logger.debug("Client: connect success")

    def send(self):
        while True:
            msg = input("Send to server ")
            self.client.sendall(msg.encode())
            logger.debug("Client : send data {}!".format(msg))

    def recv(self):
        while True:
            serverMessage = str(self.client.recv(1024), encoding='utf-8')
            logger.debug("Client : recv data!")
            if self.dtaq.full():
                self.dtaq.pop()
                logger.debug("Client_dataqueue: full!")
            self.dtaq.put(serverMessage)
        self.client.close()

if __name__ == '__main__':
    conn = Client_socket("192.168.56.104", 1203)