#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#list Comprehensions，快速生成list的方法
#eg：
"""
squares = []
for x in range(10):
	squares.append(x**2)
"""
#上面的方法可以用下面这种方式实现
squares = [x**2 for x in range(10)]
print(squares)
#同理，条件都可以在list中直接实现
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)
#也可以支持复杂的表达式
from math import pi
pai = [str(round(pi,i)) for i in range(6)]
print(pai)
