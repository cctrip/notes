#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


#写入以下代码，可以直接用python moudles.py arguments的方式执行
#python fibo.py 100
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

