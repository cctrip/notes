#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: CC

#syspath
"""
当一个名为spam的module被import时，解释器首先从内置的module查找是否有相同命名的module，
如果没有找到，解释器会从变量sys.path指定的目录列表中寻找名为spam.py的文件。
sys.path在以下情况中被初始化：
1)包含input脚本的目录(或者没有指定文件的当前目录)
2)PYTHONPATH(用于指定目录的变量，与shell中的PATH一样)
3)安装依赖时默认的设定

在初始化后，sys.path也可能被改变，该目录下的脚本会优先于标准库被搜索到和运行，
这意味着，该目录下如果有和标准库相同的名字的脚本会被优先加载，这可能造成错误，除非该替换我们已经意识到了。
"""

#编译过程：
"""
当一个modules被加载时，python会快速的在__pycache__目录中生成一个以modules.version.pyc命名的文件，
version通常是python的版本号.以spam为例就是__pycache__/spam.cpython-35.pyc
python会自动检查源数据的编译版本和当前版本是否相同，如果不相同就重新编译
编译完的modules具有平台独立性，因此同一个库可以在不同架构的系统上运行

python在以下情况不会检查cache
1)从命令行中直接加载，总是重新编译但不存储结果的module
2)没有源码module,(编译完的modules存储在源码目录中)
"""

#一些知识
"""
1)可以使用-O和-OO参数来减少编译后的modules的大小，-O可以移除"assert statements"，-OO可以移除"assert statements"和"__doc__ strings".
	“Optimized” modules have an opt- tag and are usually smaller.
2)一个程序运行时的速度，通过读取.py文件一定比通过读取.pyc文件快，.pyc文件只有在被加载的时候最快。
3)compileall modules 可以创建所有的modules的.pyc文件，并放置在同一个目录。
"""



