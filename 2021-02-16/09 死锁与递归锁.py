# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 死锁与递归锁

"""
当你知道锁的使用， 抢锁必须要释放锁， 其实你在操作锁的时候也及其容易产生死锁现象（整个程序卡死 阻塞）


"""
from threading import Thread, Lock, RLock
import time
# mutexA = Lock()
# mutexB = Lock()
mutexA = mutexB = RLock()
# 类只要加括号多次产生的肯定是不同的对象
# 如果你想要的实现多次加括号等到的是相同的对象，需要使用单例模式

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print(f'{self.name} 抢到A锁') #获取当前线程名
        mutexB.acquire()
        print(f'{self.name} 抢到B锁')
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print(f'{self.name} 抢到B锁') #获取当前线程名
        time.sleep(2)
        mutexA.acquire()
        print(f'{self.name} 抢到A锁')
        mutexA.release()
        mutexB.release()
if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
"""
递归锁的特点
可以被连续的acquire 和 release
但是只能被第一个抢到这把锁执行上述操作
他的内部有一个计数器，每acquire一次计数加一，每release一次计数减1
只要计数不为0， 那么其他人都无法抢到该锁
"""