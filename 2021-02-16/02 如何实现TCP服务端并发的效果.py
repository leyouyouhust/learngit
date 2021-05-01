# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 02 如何实现TCP服务端并发的效果

import socket
from threading import Thread
from multiprocessing import Process
"""
服务端：
    1.要有固定的IP和PORT
    2.24小时不间断提供服务
    3.能够支撑并发
    
"""

server = socket.socket() # 括号内不加参数默认为TCP
server.bind(('127.0.0.1', 8888))
server.listen(5)

# 将服务的代码单独封装成一个函数
def talk(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionError as e:
            print(e)
            break
    conn.close()

# 链接循环
while True:
    conn, addr = server.accept()   # 接客
    # 叫其他人服务
    # t = Thread(target=talk, args=(conn,))
    # t.start()
    p =Process(target=talk, args=(conn,))
    p.start()