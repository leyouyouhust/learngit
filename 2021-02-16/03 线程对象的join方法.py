# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 线程对象的join方法

from threading import Thread
import time
def task(name):
    print(f'{name} is running')
    time.sleep(3)
    print(f'{name} is over')

if __name__ == '__main__':
    t = Thread(target=task, args=('egon',))
    t.start()
    t.join() # 主线程等待子线程运行结束再执行
    print('主')