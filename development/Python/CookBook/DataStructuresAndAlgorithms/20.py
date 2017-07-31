#!/usr/bin/env python
# -*- coding: utf-8 -*-

#collections模块中的ChainMap类可以实现关联两个字典的操作

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)
print(c['x']) 
print(c['y'])
print(c['z'])

#增加
c = c.new_child()
c['x'] = 2
print(c)
