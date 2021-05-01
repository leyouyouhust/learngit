# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 10 信号量
"""
信号量在不同的阶段可能对应 不同的技术点
在并发编程中信号量指的是锁

如果我们将互斥锁比喻成一个厕所的话
那么信号量就相当于多个厕所


"""
from threading import Thread, Semaphore
import time
import random

sm = Semaphore(5)  # 括号内写数字，写几就代表几个坑位

def task(name):
    sm.acquire()
    print(f'{name} 正在蹲坑')
    time.sleep(random.randint(1, 5))
    sm.release()

if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task, args=(f'伞兵{i}号',))
        t.start()


