#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

更改PG日志格式

"""

import sys
import codecs
import re


p = re.compile("\s+")
content = ""

with codecs.open('old.csv', 'r', encoding='utf-8') as f:
    with codecs.open('new.csv', 'w', encoding='utf-8') as g:
        for line in f:
            if "2017-02-20" in line:
                g.write(content + "\n")
                content = ""
            line = re.sub(p, ' ', line)
            content = content + line.rstrip()
