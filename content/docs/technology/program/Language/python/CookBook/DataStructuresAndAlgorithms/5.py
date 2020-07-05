#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

"""
函数heapq.heappush()和 heapq.heappop()以列表_queue的方式插入和删除Item.
使得列表中的第一个Item具有最小的优先级.
heappop()方法总是返回最小项
"""

class PriorityQueue:
    """docstring for ClassName"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()


q.push(Item('aaa'), 2)
q.push(Item('bbb'), 3)
q.push(Item('ccc'), 1)
print(q.pop())
