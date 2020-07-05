#!/usr/bin/env python
# -*- coding: utf-8 -*-

#operator模块的itemgetter函数可用于此类排序

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

#sorted方法排序列表
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

#min和max方法，获取最大，最小的列表
min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))