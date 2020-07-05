#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#break,可以结束当前的for或者while循环，在循环过程中,加入break即可
#eg:
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"equals",x,"*",n//x)

print("------have break-----")
for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n,"equals",x,"*",n//x)
			break


#continue,结束该次循环，执行下次循环，在当前循环语句中加入continue即可
#eg：
for num in range(2,10):
	if num%2 == 0:
		print("Found an even number",num)
		continue
	print("Found a number",num)


#pass,在结构体当中，执行语句不能为空，否则会报错，pass的作用就是不执行任何语句，但需要手动结束任务Ctrl+c。
#eg：
while True:
	pass            
