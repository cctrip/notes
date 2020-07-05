#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#dictionary,字典，以(key/value)的方式存储数据，格式为dict = {k1:v1,k2:v2,...}
#eg：
no = {"Jack":1,"Tom":11,"Marry":22}
print(no)
#可通过key来查看value，dict[key]
print(no["Jack"])
#del可用来删除数据，用过del dict[key]的方式
del no["Tom"]
print(no)
#新增数据，可以直接使用dict[key] = value的方式
no["Helen"] = 33
print(no)
#使用list(dict.keys()),可以将key以list方式返回值
print(list(no.keys()))
#dict是无序的，若要对dict进行排序，可以使用sorted(dict.keys())，将以key进行排序
print(sorted(no.keys()))
#使用(in)可以查看key是否存在，存在返回True，不存在返回False
print("Jack" in no)
print("Tom" not in no)

#其他生产字典的方式
#用dict()函数，格式为:dict([(k1,v1),(k2,v2)...])
program = dict([("C",1),("Java",2),("Python",3)])
print(program)


#字典中的循环
#使用items()方法，可以同时获取key和value的值
for k,v in program.items():
	print(k,v)


