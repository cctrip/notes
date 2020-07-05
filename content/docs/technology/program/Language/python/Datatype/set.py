#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#set数据类型：该数据类型的值是无序的，不重复的，可以用{}和set()来定义，如果是创建一个空的set，必须使用set()
#eg：
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
#使用set()定义时，最多只能传入一个参数，set会自动分离该参数里面的值
a = set('appleadsafdfa')
b = set('dsfsafsdfsjflkllui')
print(a)
print(b)
print(a-b)
