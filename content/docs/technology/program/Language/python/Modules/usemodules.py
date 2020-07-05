#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Modules，模型，是将一部分具有类似功能的函数定义在一个.py的文件中，供其他程序进行调用
#使用方法1：import _modules_
import fibo
#调用函数的方式：
print("----first----")
a = fibo.fib
a(100)

print("----second----")
fibo.fib(200)

#使用modules.__name__可以查看名称
print(fibo.__name__)

#使用方法二：from _modules_ import _function_
from fibo import fib
#此方法可以直接使用函数名进行调用
fib(300)


#使用方法三：from _modules_ import *
#导入所有
from fibo import *
print(fib2(400))
