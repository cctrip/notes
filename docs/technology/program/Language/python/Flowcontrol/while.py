#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#while循环，指当满足条件时，就执行语句。格式为:while CONDITION: statement
#eg：
a,b=0,1
while b < 100:
	print(b)
	a,b=b,a+b
	
#end可以在一个输出过后，避免换行，用其他符号进行替代
#eg：
a,b=0,1
while b < 100:
        print(b,end=',')
        a,b=b,a+b
