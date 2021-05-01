# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 04 同一个进程下多个线程数据共享


from threading import Thread
import time
money = 100

def task():
    global money
    money = 666
    print(money)

if __name__ == '__main__':
    t =Thread(target=task)
    t.start()
    t.join()
    print(money)