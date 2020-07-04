#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#输出格式化的方法，
"""
1)string.format()
2)str()
3)repr()
"""
#str()返回一个用户习惯的阅读方式的值，repr()返回可以让解释器读取的值
s = 'hello,world\n'
print("-----str()-----")
print(str(s))
print("-----repr()-----")
print(repr(s))


#str.rjust()，右对齐，str.ljust()，左对齐，str.center()，中对齐
print("-----repr().rjust()-----")
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')  #rjust(n)方法会用空格补齐,n表示最大长度
	print(repr(x*x*x).rjust(4))



print("-----str.format()------")
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#str.zfill(),在左边用0补齐
print("----str.zfill(n)----")
print('12'.zfill(5))
print('-3.14'.zfill(7))


#string.format(),
#默认形式
print("{} and {}".format("eggs","spam"))
#下标形式
print("{1} and {0}".format("eggs","spam"))
#关键字形式
print("{food} and {drinks}".format(food="eggs",drinks="coco"))
#使用!a(ascii()),!s(str()),!r(repr()),可以在格式化前进行转换
import math
print("The vaule of PI is approximately {!r}.".format(math.pi))
#使用{:}可以指定格式化后的大小
print("The value of PI is approximately {0:.3f}.".format(math.pi))


#旧版本格式化方式
#%，eg：
print('The value of PI is approximately %0.3f.' % math.pi)
