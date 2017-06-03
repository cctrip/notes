# 编程基础

### 编程语言

* 解释型语言

        程序由解释器读取并执行
        SoucreCode --> Interpreter --> Output

* 编译型语言

        程序被编译器翻译成机器语言后再执行
        SourceCode --> Compliler --> ObjectCode --> Executor --> Output

***

### 什么是程序？

程序是指定如何执行计算的指令序列。

不同的编程语言具有一些共同的基础特性：
* input：从键盘，文件或者其他输入设备中获取数据。
* output：在屏幕显示数据，或者将数据发送给文件或者输出设备。
* math：执行基本的数学运算，比如加法和乘法
* conditional execution：检查条件并执行相应的代码
* repetition：反复执行一些操作
编程可以视为将大型的复杂任务打破成更小和更小的子任务，直到子任务简单到足以执行上述的基本操作的过程。

***

### 调试(debugging)

编程容易出错。编程错误被称为错误，并且跟踪它们的过程称为调试。
* Syntax errors：语法错误(语法是指程序的结构和关于该结构的规则)。
* Runtime errors(exceptions)：运行时错误(异常)。
* Semantic errors：语义错误，做的不是你想要让它做的事情。
调试是通过更改程序去发现和解决错误。

***

### 数据类型(type)
* interger：整数，例如1,2
* string: 字符串，例如'Hello'

***

### 变量(variables)
变量是引用值的名称，编程语言最强大的功能之一就是操纵变量的能力。
* variable：变量名，由字母开头并由字母或数字组成。最好由小写字母开头。
* keyword：关键字，用于识别程序的结构，它们不能用作变量名称。例如,if,for,while

***

### 运算符(operators)和操作数(operands)
* operators：运算符，表示计算的特殊符号，例如+,-,*
* operands：操作数

***

### 表达式(expressions)和语句(statements)
* expression：表达式，是值、变量和运算符的组合。
* statement：语句是可执行的代码单元。

***

### 注释(comments)
在程序中添加笔记，用于解释程序正在做什么

***

### 流程控制(control flow)
在程序运行时，控制个别的指令运行的顺序。

控制结构：控制结构开始时多半都会有特定的关键字，以标明使用哪一种控制结构
* choice：选择结构
    * if-then-else：
    * switch
    * case
* loop：循环结构
    * for
    * while

***

### 函数(functions)
函数是组织好的，可重复使用的，用于实现单一或相关联功能的代码段。

* function call：函数调用，一些语言一般由很多内置的函数可供调用。例如，type(32)
* function definition：定义函数，例如，def hello(): print('Hello,World!')
* flow of execution：执行流程，程序总是从第一行开始按序执行语句，函数内部的语句并不会被执行，直到函数被调用。
* parameter：参数，函数中用于供外部传入值的变量名。
* why function?：
    * 便于程序阅读
    * 消除重复代码
    * 便于调式功能
    * 便于重用

***

### 模块(Modules)

