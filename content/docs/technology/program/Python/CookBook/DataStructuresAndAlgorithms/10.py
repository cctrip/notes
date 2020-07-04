#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1,3,4,2,8,15,2,4,3]
print(list(dedupe(a)))


#list包含dict
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        print(val)
        if val not in seen:
            yield item
            seen.add(val)

b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe2(b, key=lambda d: (d['x'],d['y']))))