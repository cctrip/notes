#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

s = Stock('ACME', 100, 123.45)

print(s)

#替代
s = s._replace(shares=75)
print(s)