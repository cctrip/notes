#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq


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


q = PriorityQueue()

q.push('aaa', 2)
q.push('bbb', 3)
print(q.pop())
