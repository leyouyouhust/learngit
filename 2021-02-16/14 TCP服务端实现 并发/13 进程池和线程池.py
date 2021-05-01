# --*--coding: utf-8--*--
# @Time: 2021/2/16
# @Author: Leander
# @File: 13 进程池和线程池

"""
先看文件夹的服务端和客户端
每来一个人就开设一个进程或者线程去处理

无论是开设进程也好开设线程也好，是不是都需要消耗资源
只不过开设线程的消耗比开设进程的稍微小一点而已

我们是不可能呢做到无限制的开设进程和线程的，因为计算机硬件的资源跟不上
硬件的开发速度永远赶不上软件啊
我们的宗旨应该是在保证计算机硬件能够正常工作的情况下最大限度地利用它

"""

# 池的概念

"""
什么是池
    池是用来保证计算机硬件安全的情况下最大限度地利用计算机
    它降低了程序的运行效率，但是保证了计算机硬件的安全，从而让你写的程序能够正常运行
"""


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
import time

# pool = ThreadPoolExecutor(5)  # 池子里面固定只有5个线程

# 括号内可以传数字，代表池子造出来以后里面会固定存在五个线程，
# 这五个线程出现重复创建和销毁的过程
pool = ProcessPoolExecutor(5)
# 括号内可以传数字, 不传的话默认会开启当前计算机cpu个数个进程
# 池子的使用非常的简单，你只需要将需要的任务往池子中提交即可，自动会有人来服务你
def task(n):
    print(n, os.getpid())
    time.sleep(2)
    return n**n

def call_bakc(n):
    print('call_back', n.result())
"""
任务的提交方式
    同步：提交任务之后原地等待任务的返回结果，期间不做任何事
    异步：提交任务之后不等待任务的返回结果，继续往下执行
        返回结果如何获取
        异步提交任务的返回结果应该通过回调机制来获取
        回调机制
            就相当于给每个异步任务绑定一个定时炸弹
            一旦该任务有结果立刻触发
"""
# pool.submit(task, 1) # 朝池子中提交任务  是异步提交
# print('主')

# for i in range(20): #朝池子中提交20个任务
#     res = pool.submit(task, i)
#     print(res.result())  # result 方法，  变成了同步提交

# 于是上述代码有需要变成以下代替
if __name__ == '__main__':

    t_list = []
    for i in range(20): #朝池子中提交20个任务
        # res = pool.submit(task, i)
        res = pool.submit(task, i).add_done_callback(call_bakc)
        t_list.append(res)

    # 等待线程中所有的任务执行完毕之后在继续往下执行
    # pool.shutdown()  # 关闭线程池，但有任务没有完成会先等待池中任务完成
    # for t in t_list:
    #     print('>>>: ', t.result())  # 肯定是有序的


    """
    用result方法之后程序由并发编程了串行
    """




