#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#Packages是Python的一种结构化目录，使得我们可以以A.B.C的形式进行import
#eg：
"""
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
"""
"""
当packages被import时，python会通过sys.path去寻找它的子目录
__init__.py，是一个默认在package中定义的文件，可以为空，但必须存在，这样python才会将该目录定义为一个package
"""
#使用echo.py
import sound.effects.echo
#或者
from sound.effects import echo
#import echo中定义的函数
from sound.effects.echo import echofilter



#importing * from packages
#我们若想import packages中所有的模块，就需要在__init__.py中定义一个变量__all__
#__all__ = ["echo", "surround", "reverse"]
from sound.effects import *






