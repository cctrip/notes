#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#内置的dir()函数可以用来查找modules定义的函数，返回一个有序的string列表

import fibo,sys,builtins

print("----fibo defines----")
print(dir(fibo))
print("----sys defines-----")
print(dir(sys))


print("----arguments----")
a = [1,2,3,4]
fib = fibo.fib

print(dir())
print("----builtins---")
print(dir(builtins))
