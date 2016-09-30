#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#用户可以自定义异常，通过创建一个异常类来定义 
#eg：
class MyError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

