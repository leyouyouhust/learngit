# --*--coding: utf-8--*--
# @Time: 2021/2/15
# @Author: Leander
# @File: 知识扩展

data = 'hello world'

# 字符串转二进制
data = bytes(data, encoding='utf-8')
print(data)

# 二进制转字符串
data = str(data, encoding='utf-8')
print(data)