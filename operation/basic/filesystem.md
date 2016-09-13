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

	* Group Descriptions

	* Block Bitmap

	* Inode Bitmap

	* Inode Table

	* Data Blocks

![](ext2.gif)

***

### Inode Table

* Mode

* Owner info

* Size

* Timestamps

* Direct Blocks

* Indirect Blocks

* Double Indirect

* Triple Indirect

![](ext2_inode.gif)