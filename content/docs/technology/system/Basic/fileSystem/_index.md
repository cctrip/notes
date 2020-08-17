---
weight: 2
title: "文件系统"
bookToc: false
---

# 文件系统

文件系统是一套实现了数据的存储、分级组织、访问和获取等操作的抽象数据类型（Abstract data type）。

### 概念

文件系统是一种用于向用户提供底层数据访问的机制。它将设备中的空间划分为特定大小的块（或者称为簇），一般每块512字节。数据存储在这些块中，大小被修正为占用整数个块。由文件系统软件来负责将这些块组织为文件和目录，并记录哪些块被分配给了哪个文件，以及哪些块没有被使用。

***

### EXT2文件系统

EXT2文件系统是Linux底下最常用的文件系统。其结构如下：

* Boot Sector
	
	启动扇区，这个启动扇区可以安装启动管理程序， 这是个非常重要的设计，因为如此一来我们就能够将不同的启动管理程序安装到个别的文件系统最前端，而不用覆盖整颗硬盘唯一的MBR.

* Block Group

	* Super Block

		记录整个filesystem相关信息

	* Group Descriptions

		描述每个 block group 的开始与结束的 block 号码，以及说明每个区段 (superblock, bitmap, inodemap, data block) 分别介于哪一个 block 号码之间

	* Block Bitmap

		记录使用和未使用的block号码

	* Inode Bitmap

		记录使用和未使用的inode号码

	* Inode Table

	* Data Blocks

		数据块，实际存储数据的地方

![](ext2.gif)

***

### Inode Table

inode是ext2文件系统的基本构建块，每个文件和目录都有唯一一个inode。其机构如下：

* Mode

	存取模式信息(read/write/excute)

* Owner info

	拥有者与群组信息

* Size

	文件的容量

* Timestamps

	* 创建或状态改变的时间(ctime)

	* 最近一次的读取时间(atime)

	* 最近修改的时间(mtime)

* Direct Blocks

	12个直接指向block号码

* Indirect Blocks

	间接指向，记录block号码的记录区

* Double Indirect

	双间接指向

* Triple Indirect

	三间接指向

![](ext2-inode.gif)

***

### Super Block

Super Block是记录整个filesystem相关信息的地方，包括以下：

* Magic Number

* Revision Level

* Mount Count and Maximum Mount Count

* Block Group Number

* Block Size

* Blocks per Group

* Free Blocks

* Free Inodes

* First Inode

***

### 目录和文件

* 目录

	当我们在 Linux 下的 ext2 文件系统创建一个目录时， ext2 会分配一个 inode 与至少一块 block 给该目录。其中，inode 记录该目录的相关权限与属性，并可记录分配到的那块 block 号码； 而 block 则是记录在这个目录下的文件名与该文件名占用的 inode 号码数据。

* 文件

	我们在 Linux 下的 ext2 创建一个一般文件时， ext2 会分配一个 inode 与相对于该文件大小的 block 数量给该文件。

