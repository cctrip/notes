#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#tuple，跟list类似，都是定义一个列表，只是tuple定义后，无法被改变,定义格式:tuple = (v1,v2,v3....)
#eg：
t = (1,2,3,4,5)
print(t)
#t[0] = 10 会报错

#tuple也可以嵌套tuple类型的数据
a = (t,(6,7,8))
print(a)

#实际上，tuple可以包含变量，所以也不能完全说不能改变，只需改变变量的值，就能使得tuple发生变化
b = [2,3,4]
c = (6,b)
print(c)
b.append(7)
print(c)
