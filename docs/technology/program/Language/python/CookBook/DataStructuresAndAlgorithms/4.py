#!/usr/bin/env python
# -*- coding: utf-8 -*-

# heapq的nlargest和nsmallest可用于获得一个集合中的最大或者最小的n个数


import heapq

nums = [1, 3, 31, 5, 8, -2, 88, 93, 65, 31, 46, 111]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 也可接受一个参数，用于更复杂的数据

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(expensive)
print(cheap)


