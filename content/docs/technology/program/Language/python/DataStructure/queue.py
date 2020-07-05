#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Queue，队列，是一种"先进先出"的执行方式
#使用collections.deque可以在两边实现快速的添加和删除
#eg:
from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
print("Terry arrives")
print(queue)
queue.append("Tom")
print("Tom arrives")
print(queue)
queue.popleft()
print("The first arrives now leaves")
print(queue)
queue.popleft()
print("The second arrives now leaves")
print(queue)
