#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#字典中的循环
#使用items()方法，可以同时返回key和value的值
print("-----dictionroy loop------")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k,v)


#列表中的循环
#使用函数enumearte()，可以同时返回列表中的下标和值
print("-----list loop-----")
character = ['aa','bb','cc']
for i,v in enumerate(character):
	print(i,v)


#若要同时获取两个或多个列表的值，可以使用zip()函数
print("-----more list loop------")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
	print("What's your {0}?  It's {1}".format(q,a))

#列表反向循环可以通过reversed()函数实现
for i in reversed(range(10)):
	print(i)


#列表排序可以通过sorted()函数实现
basket = ['apple', 'orange', 'pear', 'banana']
for f in sorted(basket):
	print(f)
