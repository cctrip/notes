#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Exceptions：异常，在执行过程检测到的错误但不是致命的。最后一行的错误信息表明了发生的错误
#eg：
10 * (1/0)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""

4 + spam*3
"""
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
"""

'2' + 2
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
"""

#错误类型的名字是在创建内置的异常时产生的，用户自定义的异常不一定是正确的。
