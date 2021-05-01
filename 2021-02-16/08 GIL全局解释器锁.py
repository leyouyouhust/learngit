# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 08 GIL全局解释器锁

"""
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple
native threads from executing Python bytecodes at once. This lock is necessary mainly
because CPython’s memory management is not thread-safe. (However, since the GIL
exists, other features have grown to depend on the guarantees that it enforces.)
"""
# python 解释器有多个版本：
# CPython
# JPython
# Pypypython
# 但是普遍使用CPython

# 结论：在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，无法利用多核优势
# 在CPython解释器中GIL是一把互斥锁，用来阻止同一个进程下的多个线程的同时执行
# 同一个进程下的多个线程无法利用多核优势！！！
# 疑问：python 的多线程是不是一点用都没有？？无法利用多核优势

# 因为cpython中的内存管理不是线程安全的
# 内存管理（垃圾回收机制）
# 1.引用计数
# 2.标记清除
# 3.分代回收
# 重点：
"""
 1. GIL不是python的特点而是CPython解释器的特点
 2. GIL是保证解释器级别的数据的安全
 3. 同一个进程下的多个线程无法同时执行
 4. 针对不同的数据还是需要加不同的锁处理，
 5. 解释型语言的通病：同一个进程下多个线程无法利用多核优势
"""

# GIL与普通互斥锁的区别

# from threading import Thread, Lock
# import time
#
# mutex = Lock()
# money = 100
#
# def task(mutex):
#     global money
#     with mutex:
#         tmp = money
#         time.sleep(0.1)
#         money = tmp - 1
#
#
# if __name__ == '__main__':
#     t_list = []
#
#     for i in range(100):
#         t = Thread(target=task, args=(mutex,))
#         t.start()
#         t_list.append(t)
#
#     for t in t_list:
#         t.join()
#
#     print(money)
"""
100个线程启动之后先抢GIL
然后进入IO， GIL自动释放，但是我手上还有一把我自己的互斥锁
其他线程虽然抢到了GIL，但抢不到互斥锁
最终GIL还是回到你的手上，你去操作数据
"""

### 同一个进程下的多线程无法利用多核优势，是不是没有用了

"""
多线程是否有用要看具体情况
单核：四个任务（IO密集型\计算密集型）
多核：四个任务（IO密集型\计算密集型）
"""
# 计算密集型 每个任务都需要10s
"""
单核：不考虑

多核：
多进程：总耗时10+
多线程: 总耗时40+
"""

# IO密集型 每个任务都需要10s

"""
多进程：相对浪费资源
多线程：更加节省资源
"""

# 代码验证：

# 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import os, time
#
# def work():
#     res = 1
#     for i in range(1, 100000):
#         res *= i
#
# if __name__ == '__main__':
#     l =[]
#     print(os.cpu_count()) # 获取当前计算机cpu个数
#     start_time = time.time()
#     for i in range(12):
#         p = Process(target=work)  #10.277541875839233
#         p.start()
#         l.append(p)
#         # t = Thread(target=work)  #29.187389135360718
#         # t.start()
#         # l.append(t)
#     for p in l:
#         p.join()
#
#     print(time.time() - start_time)


# IO密集型

from multiprocessing import Process
from threading import Thread
import os, time


def work():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 获取当前计算机cpu个数
    start_time = time.time()
    for i in range(100):
        # p = Process(target=work)  #10.277541875839233
        # p.start()
        # l.append(p)
        t = Thread(target=work)  # 29.187389135360718
        t.start()
        l.append(t)
    for p in l:
        p.join()

    print(time.time() - start_time)

# 总结：
"""
多进程和多线程都有各自优势
并且我们后面在写项目的时候通常可以多进程下面再开设多线程
这样的话既可以利用多核也可以减少资源消耗

"""
