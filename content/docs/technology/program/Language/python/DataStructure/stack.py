#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Stack，栈，是一种"后进先出"的执行方式，用list很容易就能实现这种方式
#eg：
stack = [3,4,5]
print(stack)
stack.append(6)
print('6 arrived')
print(stack)
stack.append(7)
print('7 arrived')
print(stack)
stack.pop()
print('7 now leaves')
print(stack)
stack.pop()
print('6 now leaves')
print(stack)
