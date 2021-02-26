#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#python的数值计算只需输入计算表达式，python会自动打印出结果
#eg：
print(1+2)
print(5-2)
print(2*3)

#python会自动判断数值类型，除法默认输出为float类型，若想输出为int类型，可使用(//)。PS：必需除数和被除数都为int类型
#eg：
print(8/2)
print(8*2.0)
print(8//2)
print(8.0//2)

#python中可以用(**)来表达幂函数
#eg：
print(5**2)   #5的2次方
print(2**7)   #2的7次方

#python中可通过(=)来赋值给变量，并通过变量进行数值计算
#eg：
width=3
height=5
print(width*height)

#如果一个变量没有进行赋值，则会抛出error
#print(n)
#NameError: name 'n' is not defined

#也可以进行混合计算，就像我们学习数学的时候一样
#eg：
print(2+3.0/3)

#在交互式模式，可以用符号(_)来表示上次执行的结果
#eg：
'''
>>> 3+2
5
>>> 2+_
7
'''

