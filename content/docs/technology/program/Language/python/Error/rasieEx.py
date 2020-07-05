#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#raise可以强制抛出一个指定的错误，若raise不加参数，则将错误原样抛出
#eg：
try:
	raise NameError('HiThere')
except NameError:
	print("An exception flew by!")
	raise

