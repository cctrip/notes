#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

# 当数量不一致时，会报错
'''
name, height, weight = data

Traceback (most recent call last):
  File "E:\PYPATH\test\1.py", line 13, in <module>
    name, height, weight = data
ValueError: too many values to unpack (expected 3)

'''


data = ['John', 170, 60, (1999, 9, 9)]
name, height, weight, birthday = data
print(name, height, weight, birthday)


# 当元素中存在列表，可当成一个元素处理，也可以细化处理
name, height, weight, (year, mon, day) = data
print(year, mon, day)

# '_'符号为任意变量

_, remain, _, _ = data
print(remain)

# 其他可迭代对象，例如字符串
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
