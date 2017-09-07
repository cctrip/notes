## Vim配置指南

##### Don't put any lines in your vimrc that you don't understand.

***

* [Colors](#1)

* [Spaces And Tabs](#2)

* [UI Config](#3)

* [Searching](#4)

* [Folding](#5)

* [Custom Movements](#6)

* [Custom Leader](#7)

* [CtrlP Settings](#8)

* [Launch Config](#9)

* [Tmux Config](#10)

* [Autogroups](#11)

* [Backups](#12)

* [Custom Functions](#13)

* [Organization](#14)

* [Wrapping It Up](#15)

***

<h4 id="1">Colors</h4>

    colorscheme badwolf  " 设置色彩方案

    systax enable        " 开启语法处理

***

<h4 id="2">Spaces & Tabs</h4>

    set tabstop=4        " 设置每个TAB的视觉空格数

    set softtabstop=4    " 设置编辑时tab的空格数

    set expandtab        " 将<TAB>符号转换为空格

***

<h4 id="3">UI Config</h4>

    set number           " 显示行号

    set showcmd          " 在vim右下方显示最后一个命令，在powerline插件内有效

    set cursorline       " 当前行高亮