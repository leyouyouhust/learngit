# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 05 线程对象属性及其他方法

from threading import Thread, active_count, current_thread
import os, time


def task():
    print('hello world', os.getpid())
    print('hello world', current_thread().name)
    time.sleep(1)

if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    print('主', active_count()) #统计当前正在活跃的线程数
    # print('主', os.getpid())
    # print('主', current_thread().name)