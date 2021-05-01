# --*--coding: utf-8--*--
# @Time: 2021/2/16
# @Author: Leander
# @File: 11 Event事件
# 一些进程、线程需要等待另外一些进程/线程运行完毕之后才能运行，类似于发射信号一样

from threading import Thread, Event

import time

event = Event() # 造了一个红绿灯

def light():
    print('红灯亮')
    time.sleep(3)
    print('绿灯亮')
    # 告诉等待红灯得人可以走了
    event.set()

def car(name):
    print(f'{name} 车正在等红灯')
    event.wait() # 等待别人给你发信号
    print(f'{name}车加油门飙车走了')

if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(20):
        t = Thread(target=car, args=(f'{i}', ))
        t.start()