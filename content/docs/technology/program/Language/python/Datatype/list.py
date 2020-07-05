#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Python可以将多个类型的数据整合到一起，不过通常是同一种类型，多个值。这种方式叫list，用符号[]括起来，中间的数值以逗号隔开
#eg：
squares = [1,4,9,16,25]
print(squares)

#list也支持下标索引
#eg：
print(squares[1])
print(squares[2:4])

#list值是可变的
#eg：
cubes= [1,8,27,65,125]
print(cubes)
cubes[3]=64    #更改65为64
print(cubes)
print(cubes+[216,343])  #添加值和cubes一起作为输出
print(cubes)

#上面添加的方式不会改变cubes的值，若要添加到cubes中，可以用list.append()的方式，会将值默认添加到最后一位
#eg：
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

#当替换的值为空时，可以用来移除list中的值
#eg：
cubes[5:] = []
print(cubes)

#len()函数也可以计算list的长度
#eg：
len(cubes)

#list中还可以包含list的类型
a = [1,2,3]
b = ['x','y','z']
c = [a,b]
print(c)


#list的各种方法：
"""
list.append(x)：在末尾加入一条数据
list.extend(L)：
list.insert(i,x)：在指定位置插入一条数据，其位置后面的所有数据默认后移一位
list.remove(x)：移除第一个值为x的数据
list.pop([i])：移除指定位置的数据，若没有指定i，默认移除最后一位
list.clear()：清除所有数据
list.index(x)：获取第一个值为x的下标号码
list.count(x)：获取值为x的个数
list.sort(key=None,reverse=false)：按顺序排列list的值
list.reverse()：反向排列list的值
list.copy()：拷贝一个list
"""
num = [0,3,9]
num.append(4)
print(num)
num.insert(0,1)
print(num)
num.sort()
print(num)
num.reverse()
print(num)
num.remove(4)
print(num)
num.pop(0)
print(num)
print(num.index(3))
print(num.count(3))
num.clear()
print(num)

