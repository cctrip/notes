#!/usr/bin/env python
# -*- coding: utf-8 -*-

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}


#获取最大、小值和其名称
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

#排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))


#只获取最大、小值
min(prices.values())
max(prices.values())

#只获取最大、小值的名称
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

