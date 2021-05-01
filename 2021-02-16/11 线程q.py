# --*--coding: utf-8--*--
# @Time: 2021/2/16
# @Author: Leander
# @File: 11 线程q

"""
同一个进程下多个线程数据是共享的
为什么在同一个进程下还会去使用队列呢

因为队列是
    管道 + 锁
所以用队列还是为了保证数据的安全

"""

import queue
# 我们现在使用的队列都是只能在本地测试使用

# 1. 队列q 先进先出

# q = queue.Queue(3)
# q.put(1)
# q.get()
# q.get_nowait()
# q.get(timeout=3)
# q.full()
# q.empty()

# 后进先出q

# q = queue.LifoQueue() # last in first out
#
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())  #3


# 优先级q  你可以给放入队列中的数据设置进出的优先级

q = queue.PriorityQueue(4)
q.put((10, '111'))
q.put((100, '222'))
q.put((0, '333'))
q.put((-5, '444'))
print(q.get())  # (-5, '444')
# put 传入参数为元组，第一个为数字代表优先级，第二位数据，数字越小优先级越高
