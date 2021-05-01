# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 07 线程互斥锁

from threading import Thread, Lock
import time
money = 10
mutex = Lock()
def task(mutex):
    global money
    mutex.acquire()
    tmp = money
    time.sleep(1)
    money = tmp - 1
    mutex.release()

if __name__ == '__main__':
    t_list = []

    for i in range(10):
        t = Thread(target=task, args=(mutex,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print(money)