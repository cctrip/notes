#!/usr/bin/env python
# -*- coding: utf-8 -*-

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

pos = [n for n in mylist if n > 0]
print(pos)


#复杂处理

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

#另一个值得注意的过滤工具是itertools.compress（），
#它将一个可迭代和一个随附的布尔选择器序列作为输入。
#作为输出，它给出了iterable中所有选项中相应元素为True的项

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
