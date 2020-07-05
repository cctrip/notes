#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#if条件判断，当满足条件，执行语句。格式为：if CONDITION: statement elif CONDITION: statement else: statement 
#eg：
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print("Negative changed to zero")
elif x == 0:
	print("Zero")
elif x == 1:
	print("Single")
else:
	print("More") 
