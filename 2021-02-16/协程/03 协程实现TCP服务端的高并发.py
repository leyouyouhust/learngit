# --*--coding: utf-8--*--
# @Time: 2021/2/16
# @Author: Leander
# @File: 协程实现TCP服务端的高并发
from gevent import monkey;monkey.patch_all()
import time
import socket
from gevent import spawn

def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            conn.send(data.upper())
        except ConnectionError as e:
            print(e)
            break
    conn.close()

def server(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        #开设多进程或多线程处理客户端通信
        spawn(communication, conn)
if __name__ == '__main__':
    g1 = spawn(server, '127.0.0.1', 8080)
    g1.join()

"""
我们可以通过多进程下面开设多线程
多线程下面再开设协程
从而使我们的程序执行效率提升

"""

