#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#for循环结构，按序读出list或string中的所有值，用于执行其他操作，格式：for i in lists: statement.
#eg：
words=['cat','windows','defenestrate']

for w in words:
	print(w,len(w))


#也可以通过for循环改变list的数据
for w in words[:]:
	if len(w) > 7:
		words.insert(0,w)

print(words)

#range()函数，可以生成一个有序的列表，格式为:range(init,end,add)，
#eg
print("生成0到5的数range(5)")
for i in range(5):
	print(i)


print("生成5到10的数range(5,10)")
for i in range(5,10):
	print(i)	

print("生成10到30的数，每次加2range(10,30,2)")
for i in range(10,30,2):
	print(i)
#print无法直接查看range()函数生成的所有数，可用list(range()).
#eg:
print(range(5))
print(list(range(5)))
