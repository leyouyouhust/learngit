# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 01 开启线程的两种方式
# 第一种方式
# from threading import Thread
# import time
#
# def task(name):
#     print(f'name is running')
#     time.sleep(1)
#     print(f'name is over')
#
# # 开启线程不需要在main下面执行代码 直接书写就可以
# # 但是我们还是习惯性的将启动命令写在main 下面
#
# t = Thread(target=task, args=('egon',))
# t.start()  # 创建线程的开销非常小，几乎是代码一执行线程就已经创建了
# print('主')

# 第二种方式

from threading import Thread
import time
class MyThread(Thread):
    def __init__(self, name):
        """针对双下划线开头双下划綫结尾（__init__)的方法，统一读成双下init"""
        # 重写了别人的方法，又不知道别人的方法里有啥，你就调用父类的方法
        super(MyThread, self).__init__()
        self.name = name
    def run(self):
        print(f'{self.name} is running')

if __name__ == '__main__':
    t = MyThread('egon')
    t.start()