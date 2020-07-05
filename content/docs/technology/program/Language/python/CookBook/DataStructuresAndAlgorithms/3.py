#!/usr/bin/env python
# -*- coding: utf-8 -*-

# collections.deque可用于保留有限历史记录

# 用法，from collections import deque
# deque(maxlen = n), maxlen表示要保留的长度

from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

print('-' * 20)
# 若不限制保留长度，则为无线长度

p = deque()

p.append(1)
print(p)
p.appendleft(2)
print(p)
p.append(3)
print(p)
p.pop()
print(p)
p.popleft()
print(p)
