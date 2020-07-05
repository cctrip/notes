#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

#定义dict时直接赋值
d = {
    'a':[1,2,3],
    'b':[4,5]
}
e = {
    'a':{1,2,3},
    'b':{6,5}
}    

print(d)
print(e)

#利用defaultdict定义
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)


e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)

print(d)
print(e)

#利用dict自带的setdefault定义
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)