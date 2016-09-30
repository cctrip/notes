#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#函数是代码的一种抽象方式。只需定义一次，可以反复调用。
#函数定义格式：def Name(Arguments):statement
#eg：
def fib(n):
	a,b=0,1
	while a < n:
		print(a,end=' ')
		a,b=b,a+b	
	print()
#函数调用，直接使用函数名加参数进行调用：
#eg：
fib(100)

#函数也可以重命名,类似赋值的方式，不会去更改实际的函数名，只是一个引用
#eg：
print("-------rename-------")
f = fib
f(200)
#fib依然存在
fib(300)
print("--------------------")

#可以用return来给函数一个返回值，没使用return时，自动返回None
print("------return--------")
print(fib(0))

def fib2(n):
	result = []
	a,b=0,1
	while a < n:
		result.append(a)
		a,b=b,a+b
	return result

print(fib2(400))


#使用文档注释
def my_function():
	"""
	Do nothing but document it.
	"""
	pass

#查看文档注释可以使用my_function.__doc__
print(my_function.__doc__)
