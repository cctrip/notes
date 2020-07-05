#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC


#可以对异常进行处理，使程序能正常执行，使用try....except
#eg：
"""
while True:
	try:
		x = int(input("Please enter a number: "))
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")
"""

###整个异常处理的过程
"""
1)try执行，用于捕获异常
2)如果没有发生异常，则跳过except子句的过程，执行statment(位于try..except中间)
3)若发生异常，跳过实际报错，如果该错误类型匹配except后的关键字，则执行except，然后再次执行statment
4)若不匹配错误类型，则报出实际错误
"""

#一个执行语句可能有多种错误，因此可以指定多个错误，多个错误也可以放在同一个tuple中
#eg
"""
	except (RuntimeError, TypeError, NameError):
		pass
"""
#最后一个except的关键字可以被忽略，这个方式容易隐蔽真正的程序错误，可以让你将错误以自己定义的方式重新抛出
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


#在try...except中还有个else选项，这个选项可以在没有抛出任何异常时依然执行语句

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


#try...except也可以捕获函数中的错误，将函数作为statements即可

