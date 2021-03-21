---
bookCollapseSection: false
weight: 6
title: "Go程序执行顺序"
---

# Go程序执行顺序

下面是go程序的执行顺序,[原文](https://golangbyexample.com/order-execution-program-golang/)

* 程序由main package开始
* 对main package import的package进行初始化，递归进行
* 初始化这些package定义的全局变量
* 执行这些package的init()函数
* 初始化main package的全局变量
* 执行main package的init()函数
* 执行main()函数

***

