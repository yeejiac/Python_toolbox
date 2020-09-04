import socket
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
from lib.iniparser import * 
from lib.logwriter import *
import queue 
import threading
import time


class Connection:
    def __init__(self, conn, connnum):
        self.conn = conn
        self.connnum = connnum
        self.dtaq = queue.Queue(maxsize = 10)
        t_recv = threading.Thread(target = self.recv())
        t_recv.start()
        
    def recv(self):
        while True:
            clientMessage = str(self.conn.recv(1024), encoding='utf-8')
            if not clientMessage:break
            if self.dtaq.full():
                self.dtaq.get()
                logger.debug("Server: full!")
            self.dtaq.put(clientMessage)
            logger.debug("Server: recv {}".format(clientMessage))
        logger.debug("Server: lose conn")


class Server_socket:
    def __init__(self, addr, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((addr, port))
        self.server.listen(10)
        self.connStorage = []
        self.lock = threading.Lock()
        t_conn = threading.Thread(target = self.keep_accept_connection())
        t_conn.start()

    def keep_accept_connection(self):
        while True:
            print(1)
            conn, connum = self.server.accept()
            logger.debug("Server : connect with {}!".format(connum[1]))
            
            self.lock.acquire()
            connected = threading.Thread(target = Connection, args=(conn, connum[1]))
            connected.start()
            logger.debug("Server : put {} to the storage!".format(connum[1]))
            self.connStorage.append((connected, connum[1]))
            self.lock.release()
            
        self.server.close()
            

if __name__ == '__main__':
    server = Server_socket(addr, port)
    