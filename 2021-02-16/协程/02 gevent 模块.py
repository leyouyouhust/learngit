# --*--coding: utf-8--*--
# @Time: 2021/2/16
# @Author: Leander
# @File: 02 gevent 模块

from gevent import monkey;monkey.patch_all()
import time
from gevent import spawn

"""
gevent 模块本身无法检测常见的一些IO操作
在使用的时候需要你额外的导入一句话
from gevent import monkey;monkey.patch_all()
由于上面的两句话在使用gevent模块的时候肯定要导入的所以支持简写

"""
def heng():
    print('heng')
    time.sleep(2)
    print('heng')

def ha():
    print('hhh')
    time.sleep(3)
    print('hhh')

start_time = time.time()
g1 = spawn(heng)
g2 = spawn(ha)
g1.join()
g2.join()
# heng()
# ha()
print(time.time()-start_time)
