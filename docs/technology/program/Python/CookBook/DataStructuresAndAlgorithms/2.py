#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 星号表达式可以将列表中剩余的未经赋值的元素组成另一个列表，可用于任意位置

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

*info, telephone = record
print(info)

# '*_'符号，可丢弃一段数据，只保留想要的数据

*_, telephone = record
print(telephone)
