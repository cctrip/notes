#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: CC


#open()函数可以返回一个文件目标，通常包含两个参数open(filename,mode)
"""
filename是文件名
mode有以下几种模式
r)：只读(不指定时，默认为该模式)
w)：只写(如果存在相同文件，之前的文件会被清除)
a)：添加(将数据添加到文本的尾部)
r+)：读写模式
b)：二进制模式写模式
"""
f = open("/cache1/Python/IO/file1.txt","r")

#file.read(size)，可以读取一定量的内容，下次读取从未读取完的内容开始。当size省略时，读取所有内容。如果内容被读取完，f.read()会返回一个空值('')
print("----readsize----")
print(f.read(15))
print("----readall-----")
print(f.read())

#file.readline()可以每次只读取一行的内容
print("----readline----")
f = open("/cache1/Python/IO/file1.txt","r")
print(f.readline())

#list(f),f.readlines(),都可以获取所有行，或者下面的方式
for line in f:
	print(line,end='')


#file.write()方法可以对文件进行写操作
print("-----filewrite-----")
f2 = open("/cache1/Python/IO/file2.txt","r+")
f2.write("This is test.\n")

value = ("The answer is",42,"\n")
s = str(value)
f2.write(s)

f2 = open("/cache1/Python/IO/file2.txt","r+")
print(f2.read())

#file.close()，在执行文件操作完成后，执行该方法，可以释放该文件操作的所有系统资源，执行后，再进行文件操作会报错
f.close()

#文件读写过程中，可能会报IOError，这样close就不会执行，因此引入try...finally，无论执行过程是否有问题，都进行关闭
#with可以简化这种操作
#eg
print("----with-close----")
with open("/cache1/Python/IO/file3.txt","r+") as f3:
	f3.write("hello,python!")
with open("/cache1/Python/IO/file3.txt","r+") as f3:
    print(f3.read())


#结构化数据之JSON，格式{name:value},name是一个字符串，value可以是任意组合的数据
#python中JSON的应用
#eg:json.dupms(value)：
import json
print(json.dumps([1,"all","in"]))
#json.dump(object,file),将数据写入文件中，json.load(file)，读取文件中的数据
x  = ["hey","I'm",19]
with open("/cache1/Python/IO/file4.txt","w") as f4:
	json.dump(x,f4)

with open("/cache1/Python/IO/file4.txt","r") as f4:
	print(json.load(f4))

