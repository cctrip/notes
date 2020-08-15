---
bookCollapseSection: false
weight: 1
title: "并发"
---

# 并发

## goroutine

### 和Thread的区别

* 内存消耗，创建一个 goroutine 的栈内存消耗为 2 KB，。创建一个 thread 则需要消耗 1 MB 栈内存，而且还需要一个被称为 “a guard page” 的区域用于和其他 thread 的栈空间进行隔离。

* 创建与销毀，Thread 创建和销毀都会有巨大的消耗，因为要和操作系统打交道，是内核级的，通常解决的办法就是线程池。而 goroutine 因为是由 Go runtime 负责管理的，创建和销毁的消耗非常小，是用户级。

* 切换，当 threads 切换时，需要保存各种寄存器，以便将来恢复：

  > 16 general purpose registers, PC (Program Counter), SP (Stack Pointer), segment registers, 16 XMM registers, FP coprocessor state, 16 AVX registers, all MSRs etc.

  而 goroutines 切换只需保存三个寄存器：Program Counter, Stack Pointer and BP。

***

### GPM

