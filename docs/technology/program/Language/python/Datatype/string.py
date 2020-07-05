#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#python可以通过('')和("")来操作string类型的数据，符号(\)可以用来对一些特殊符号进行转义
#eg：
print('hello,world')
print("hello,world")
print('he\'s cool')
print("he's cool")

#但是在交互式界面，符号(\)将会被当做输出，不具备转义功能，此时，就需要使用print()函数，此函数功能为输出内容到屏幕
#eg：
'''
>>> '"Isn\'t",she said.'
'"Isn\'t",she said.'
'''
print('"Isn\'t",she said.')

#一些特殊组合可以实现一些功能，例如(\n)可以实现换行,(\t)可以跳过空格
#eg：
print("hello,\nworld!")
print("hello,\tworld!")

#但有些时候，我们只想把这些特殊组合当成输出，例如(C:\some\name)，此时可以在整个string前加(r)来表示里面的内容都直接输出，不转义
#eg：
print("C:\some\name")
print(r"C:\some\name")

#要想实现多行，可以不使用(\n)进行换行，可以用("""...""")或者('''...''')来实现,为防止变成失效，最好是在行尾加上(\)符号
#eg：
print("""\
aaa
bbb
ccc""")

#多个string之间可以通过(+)符号来整合成一块，(*)符号可以重复n次该string
#eg：
print(3*"ab"+"hello")
#也可以通过空格来实现，PS：如果是包含变量不能使用这种方式，只能使用上面的方式来整合,该方式也适合长string
#eg：
print("abc" "hello")
prefix="abc"
#print(prefix "hello")
#SyntaxError: invalid syntax
print(prefix + "hello")
print("hello,world!" "hello,codecc!")

#string类型有下标索引，通过string[index],可以查找到第几个字母，index从0开始，最大长度为string的长度，超出会报错
#eg：
word="hello,world"
print(word[0])
print(word[5])
#print(word[100])
#IndexError: string index out of range

#也可以反着来，从-1开始表示倒数最后一个
#eg：
print(word[-1])
print(word[-6])

#还可以指定区间，通过(:)来实现
#eg：
print(word[0:2])  #0到2，但不包括2，若:前不指定，默认为0，:后不指定，默认到最后一个
print(word[2:])

#定义后的string是不可变的，如果需要不同的string，需要创建一个
#word[0]="K"
#TypeError: 'str' object does not support item assignment
newword= "K" + word[2:]
print(newword)

#计算字符串长度可以使用len(string)函数
#eg：
print(len(word))


#string有大量的方法可以使用，使用格式为str.method()
#eg：格式化成string类型
print('hello,{0}'.format(1+2))


