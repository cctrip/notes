#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#try statement有其他选项的子句来执行某些动作，finally是在所有语句执行完后，必须要执行的一个动作
#eg：
"""
try:
	raise KeyboardInterrupt
finally:
	print("Goodbye!")
"""

def devide(x,y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is ",result)
	finally:
		print("executing finally clause")
		

print(devide(2,2))
print(devide(1,0))
