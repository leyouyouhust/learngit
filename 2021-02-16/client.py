# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: client

import socket
client = socket.socket()
client.connect(('127.0.0.1', 8888))

while True:
    client.send(b'hello world')
    data = client.recv(1024)
    print(data.decode('utf-8'))