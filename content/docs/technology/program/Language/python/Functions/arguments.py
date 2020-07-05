#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#函数参数：
#1)位置参数：
#1、必选参数，函数定义了必选参数，则在调用时必需给参数赋值，否则会报错
#eg:
def hello(n):
	pass
#error
#hello()
hello(3)

#2、默认参数，函数在定义在参数时直接给参数赋值，若在调用时没有传入值，则该位置的参数以默认值为准
#如果不按顺序，则需要指定参数名和值
#eg：
def person(name,age=18,city='xiamen'):
	print("My name is ",name)
	print("Age is ",age)
	print("I'm from ",city)

print('-----only input name------')
person('Code')
print('----input name,age,city---')
person('CC',21,'quanzhou')

#当默认参数为一个可变的值时，例如list，则每次调用都会加上前次调用的值，若不想这样做，则可以将初始值赋值为None
#eg：
def f(a,L=[]):
	L.append(a)
	return L

print("-----first called-------")
print(f(1))
print("-----second called-------")
print(f(2))


#2)关键字参数：
#关键字参数可在传参时传入一个(参数名=值)的组合
#eg：
print('-----use keyword---------')
person(name='Caro',city='fuzhou',age=18)
#以下传参会发生错误
#person()，--没有参数值
#person(name='aa',18)  --关键字参数后面不能带不上关键字参数的值
#person('aa',name='dd')   --不能给同一个参数传入两个值
#person(home='fujian')   --未知的关键字参数

#在定义参数时，可以将最后一个参数定义为**name，此参数可以接收0到n个的关键字参数，这些关键字参数在函数内部会被自动组装成dict
#eg：
def animal(kind,**more):
	print("The animal's type is ",kind)
	keys = sorted(more.keys())  #获取dict的每个key值,将以列表形式返回
	for kw in keys:
		print(kw,":",more[kw])   #more[kw]，获取dict中key值对应的value值

print('-----**name--------')
animal('dog',name='yoyo',age=2)
#也可以传入一个定义的dict列表，传入时必须加**
lion = {'kind':'lion','name':'toto','age':3}
animal(**lion)

		
#3)可变参数：
#在定义参数时，将参数定义为*name，此参数可以接收n个参数，这些参数被组装成tuple，若与**name一起使用，则*name必须在**name之前
#eg：
def course(*args,sep='.'):
	print(args)
	print(sep.join(args))

print('-----*name------')
course('math','english','physical')
#也可传入一个变量，传入时必须加*
arg=['aa','bb','cc','dd']
course(*arg)


#参数组合：顺序，必选参数、默认参数、可变参数/命名关键字参数和关键字参数。

